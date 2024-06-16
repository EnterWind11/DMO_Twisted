from .ServerProtocol import GameProtocol  # Ensure this path is correct
from twisted.internet.protocol import Factory

class GameFactory(Factory):
    def buildProtocol(self, addr):
        return GameProtocol()
