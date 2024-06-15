import struct


class Packet:
    def __init__(self):
        self.buffer = bytearray()
        self.read_pos = 0

    # Write methods
    def write_int(self, value):
        self.buffer += struct.pack('i', value)

    def write_uint(self, value):
        self.buffer += struct.pack('I', value)

    def write_short(self, value):
        self.buffer += struct.pack('h', value)

    def write_ushort(self, value):
        self.buffer += struct.pack('H', value)

    def write_float(self, value):
        self.buffer += struct.pack('f', value)

    def write_double(self, value):
        self.buffer += struct.pack('d', value)

    def write_char(self, value):
        self.buffer += struct.pack('c', value.encode('utf-8'))

    def write_string(self, value):
        self.write_ushort(len(value))  # Write length of the string first
        self.buffer += value.encode('utf-8')

    def get_data(self):
        return bytes(self.buffer)

    # Read methods
    def read_int(self):
        value = struct.unpack_from('i', self.buffer, self.read_pos)[0]
        self.read_pos += struct.calcsize('i')
        return value

    def read_uint(self):
        value = struct.unpack_from('I', self.buffer, self.read_pos)[0]
        self.read_pos += struct.calcsize('I')
        return value

    def read_short(self):
        value = struct.unpack_from('h', self.buffer, self.read_pos)[0]
        self.read_pos += struct.calcsize('h')
        return value

    def read_ushort(self):
        value = struct.unpack_from('H', self.buffer, self.read_pos)[0]
        self.read_pos += struct.calcsize('H')
        return value

    def read_float(self):
        value = struct.unpack_from('f', self.buffer, self.read_pos)[0]
        self.read_pos += struct.calcsize('f')
        return value

    def read_double(self):
        value = struct.unpack_from('d', self.buffer, self.read_pos)[0]
        self.read_pos += struct.calcsize('d')
        return value

    def read_char(self):
        value = struct.unpack_from('c', self.buffer, self.read_pos)[0].decode('utf-8')
        self.read_pos += struct.calcsize('c')
        return value

    def read_string(self):
        length = self.read_ushort()
        value = struct.unpack_from(f'{length}s', self.buffer, self.read_pos)[0].decode('utf-8')
        self.read_pos += struct.calcsize(f'{length}s')
        return value