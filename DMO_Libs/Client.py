from twisted.internet import reactor
from .ClientProtocol import GameClient
from twisted.internet.protocol import ClientFactory

class GameClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return GameClient()

    def clientConnectionFailed(self, connector, reason):
        print(f"Connection failed: {reason}")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print(f"Connection lost: {reason}")
        reactor.stop()
