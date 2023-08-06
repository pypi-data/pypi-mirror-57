import json
import logging
import sys
from threading import Thread
from time import sleep

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol
from fbchat import log, Client, ThreadType
from fbchat.utils import Message
from twisted.internet.protocol import ReconnectingClientFactory

platform = "JarbasFaceBookBridgev0.1"
logger = logging.getLogger(platform)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel("INFO")


class FaceBot(Client):
    protocol = None

    def bind(self, protocol):
        self.protocol = protocol

    def onMessage(self, author_id, message_object, thread_id, thread_type,
                  **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        log.info("{} from {} in {}".format(message_object, thread_id,
                                           thread_type.name))

        # If you're not the author, process
        if author_id != self.uid:
            utterance = message_object.text
            if thread_type == ThreadType.GROUP:
                name = self.fetchUserInfo(self.uid)[self.uid].name
                if "@" + name.lower() not in utterance.lower():
                    return
                utterance = utterance.replace("@" + name, "")
            msg = {"data": {"utterances": [utterance],
                            "lang": "en-us"},
                   "type": "recognizer_loop:utterance",
                   "context": {"source": self.protocol.peer,
                               "destination": "hive_mind",
                               "platform": platform,
                               "user": author_id,
                               "fb_chat_id": thread_id,
                               "thread_type": thread_type.name}}
            msg = json.dumps(msg)
            msg = bytes(msg, encoding="utf-8")
            self.protocol.sendMessage(msg, False)


class JarbasFacebookBridgeProtocol(WebSocketClientProtocol):
    facebook = None
    chat_thread = None
    MAIL = ""
    PASSWD = ""

    def start_fb_chat(self):
        self.facebook = FaceBot(self.MAIL, self.PASSWD)
        self.facebook.listen()

    def onConnect(self, response):
        logger.info("[INFO] Server connected: {0}".format(response.peer))
        self.factory.client = self
        self.factory.status = "connected"
        self.MAIL = self.factory.mail
        self.PASSWD = self.factory.passwd

    def onOpen(self):
        logger.info("[INFO] WebSocket connection open. ")

        self.chat_thread = Thread(target=self.start_fb_chat)
        self.chat_thread.setDaemon(True)
        self.chat_thread.start()
        while self.facebook is None:
            sleep(1)
        self.facebook.bind(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            payload = payload.decode("utf-8")
            msg = json.loads(payload)
            utterance = ""
            if msg.get("type", "") == "speak":
                utterance = msg["data"]["utterance"]
            elif msg.get("type", "") == "server.complete_intent_failure":
                utterance = "does not compute"

            if utterance:
                user_id = msg["context"]["fb_chat_id"]
                thread_type = msg["context"]["thread_type"]
                if thread_type == "GROUP":
                    thread_type = ThreadType.GROUP
                else:
                    thread_type = ThreadType.USER
                self.facebook.send(Message(text=utterance),
                                   thread_id=user_id,
                                   thread_type=thread_type)
        else:
            pass

    def onClose(self, wasClean, code, reason):
        logger.info("[INFO] WebSocket connection closed: {0}".format(reason))
        self.factory.client = None
        self.factory.status = "disconnected"


class JarbasFacebookBridge(WebSocketClientFactory,
                           ReconnectingClientFactory):
    protocol = JarbasFacebookBridgeProtocol

    def __init__(self, mail, password, name="facebook bridge", *args,
                 **kwargs):
        super(JarbasFacebookBridge, self).__init__(*args, **kwargs)
        self.status = "disconnected"
        self.name = name
        self.client = None
        self.mail = mail
        self.passwd = password

    # websocket handlers
    def clientConnectionFailed(self, connector, reason):
        logger.info(
            "Client connection failed: " + str(reason) + " .. retrying ..")
        self.status = "disconnected"
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        logger.info(
            "Client connection lost: " + str(reason) + " .. retrying ..")
        self.status = "disconnected"
        self.retry(connector)


