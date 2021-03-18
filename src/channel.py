from src.utils import b64decoder
import base64

class Channel:
    def __init__(self, node, name):
        self.node = node
        self.name = name
        self.channel = self.node.pubsub.subscribe(self.name)

    def send(self, text):
        #creazione del messaggio di invio: metto l'id del nodo davanti
        msg = "{}|{}".format(self.node.id()['ID'], text)
        try:
            self.node.pubsub.publish(self.name, msg)
        except Exception as e:
            print(e)

    def recv(self):
        try:
            for m in self.channel:
                break
        except Exception as e:
            print(e)
        return m['from'], b64decoder(m['data'])


    def b64decoder(self, b64str):
        return base64.b64decode(b64str.encode('ascii')).decode('ascii')


