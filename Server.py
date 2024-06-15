from twisted.internet import protocol, reactor
from DMO_Libs.Packets import Packet  # Importing the Packet class from packet.py

class GameProtocol(protocol.Protocol):
    def __init__(self):
        self.packet = Packet()

    def dataReceived(self, data):
        self.packet.buffer.extend(data)
        self.process_packets()

    def process_packets(self):
        while True:
            if len(self.packet.buffer) < self.packet.read_pos + 2:
                break  # Not enough data to read packet length
            length = self.packet.read_ushort()
            if len(self.packet.buffer) < self.packet.read_pos + length:
                self.packet.read_pos -= 2  # Rewind read_pos to undo the read_ushort
                break  # Not enough data to read full packet
            # Process packet data
            print(f"Received packet: {self.packet.buffer[self.packet.read_pos:self.packet.read_pos+length]}")
            self.packet.read_pos += length

    def connectionMade(self):
        print("Connection made")

    def connectionLost(self, reason):
        print(f"Connection lost: {reason}")

class GameFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return GameProtocol()

# Example usage
if __name__ == "__main__":
    factory = GameFactory()
    reactor.listenTCP(7029, factory)
    print("Server started on port 7029...")
    reactor.run()