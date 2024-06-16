from twisted.internet import protocol
import msgpack
from .PacketID import PacketID

HEADER_SIZE = 4  # Assuming a 2-byte header for packet length

class GameProtocol(protocol.Protocol):
    def __init__(self):
        self.buffer = bytearray()

    def dataReceived(self, data):
        self.buffer.extend(data)
        self.process_packets()

    def process_packets(self):
        while len(self.buffer) >= HEADER_SIZE:  # Check if enough data for header
            packet_length = int.from_bytes(self.buffer[:HEADER_SIZE], byteorder='big')
            if len(self.buffer) >= packet_length:
                packet_data = self.buffer[:packet_length]
                self.buffer = self.buffer[packet_length:]
                self.handle_packet(packet_data)
            else:
                break

    def handle_packet(self, packet_data):
        try:
            unpacked_data = msgpack.unpackb(packet_data, raw=False)
            packet_id = unpacked_data['packet_id']
            match packet_id:
                case PacketID.LOGIN.value:
                    self.handle_login_packet(unpacked_data)
                case PacketID.SERVER_SELECTION.value:
                    self.handle_server_selection_packet(unpacked_data)
                case PacketID.CHARA_SELECTION.value:
                    self.handle_chara_selection_packet(unpacked_data)
                case PacketID.CONFIRM.value:
                    self.handle_confirm_packet(unpacked_data)
                case _:
                    print(f"Unknown packet ID: {packet_id}")
        except Exception as e:
            print(f"Error processing packet: {e}")

    def handle_login_packet(self, data):
        username = data.get('username')
        password = data.get('password')
        print(f"Login packet received: username={username}, password={password}")
        self.send_response({'packet_id': PacketID.CONFIRM.value, 'message': "Login successful"})

    def handle_server_selection_packet(self, data):
        server_id = data.get('server_id')
        print(f"Server selection packet received: server_id={server_id}")
        self.send_response({'packet_id': PacketID.CONFIRM.value, 'message': "Server selection confirmed"})

    def handle_chara_selection_packet(self, data):
        character_id = data.get('character_id')
        print(f"Character selection packet received: character_id={character_id}")
        self.send_response({'packet_id': PacketID.CONFIRM.value, 'message': "Character selection confirmed"})

    def handle_confirm_packet(self, data):
        print("Confirm packet received")
        self.send_response({'packet_id': PacketID.CONFIRM.value, 'message': "Action confirmed"})

    def send_response(self, data):
        packed_data = msgpack.packb(data)
        self.transport.write(packed_data)

    def connectionMade(self):
        print("Connection made")

    def connectionLost(self, reason):
        print(f"Connection lost: {reason}")

class GameFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return GameProtocol()
