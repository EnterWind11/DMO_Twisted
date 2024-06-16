from twisted.internet import reactor
from DMO_Libs.Server import GameFactory
from DMO_Libs.Client import GameClientFactory

# Constants
SERVER_IP = '127.0.0.1'
SERVER_PORT = 7029

# Entry point for both server and client
if __name__ == "__main__":
    # Start server
    reactor.listenTCP(SERVER_PORT, GameFactory())

    # Connect client
    reactor.connectTCP(SERVER_IP, SERVER_PORT, GameClientFactory())

    # Run the Twisted reactor
    reactor.run()