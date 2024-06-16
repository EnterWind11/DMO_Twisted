from twisted.internet import protocol
from twisted.internet import reactor
from .PacketsData import Packet
from .PacketID import PacketID

class GameClient(protocol.Protocol):
    def connectionMade(self):
        print("Connection made to the server")
        self.send_login_packet()

    def dataReceived(self, data):
        packet = Packet()
        packet.load_data(data)

        packet_id = packet.read_ushort('packet_id')

        if packet_id == PacketID.CONFIRM.value:
            message = packet.read_string('message')
            print(f"Server response: {message}")
        else:
            print(f"Unknown packet ID: {packet_id}")

    def send_packet(self, packet):
        self.transport.write(packet.get_data())

    def send_login_packet(self):
        packet = Packet()
        packet.write_ushort('packet_id', PacketID.LOGIN.value)
        packet.write_string('username', "my_username")
        packet.write_string('password', "my_password")
        self.send_packet(packet)

    def send_server_selection_packet(self):
        packet = Packet()
        packet.write_ushort('packet_id', PacketID.SERVER_SELECTION.value)
        packet.write_int('server_id', 1)
        self.send_packet(packet)

    def send_chara_selection_packet(self):
        packet = Packet()
        packet.write_ushort('packet_id', PacketID.CHARA_SELECTION.value)
        packet.write_int('character_id', 42)
        self.send_packet(packet)

    def send_confirm_packet(self):
        packet = Packet()
        packet.write_ushort('packet_id', PacketID.CONFIRM.value)
        self.send_packet(packet)

    def connectionLost(self, reason):
        print(f"Connection lost: {reason}")

class GameClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return GameClient()

    def clientConnectionFailed(self, connector, reason):
        print(f"Connection failed: {reason}")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print(f"Connection lost: {reason}")
        reactor.stop()
