import msgpack

class Packet:
    def __init__(self):
        self.data = {}

    def write_int(self, key, value):
        self.data[key] = value

    def write_uint(self, key, value):
        self.data[key] = value

    def write_short(self, key, value):
        self.data[key] = value

    def write_ushort(self, key, value):
        self.data[key] = value

    def write_float(self, key, value):
        self.data[key] = value

    def write_double(self, key, value):
        self.data[key] = value

    def write_char(self, key, value):
        self.data[key] = value

    def write_string(self, key, value):
        self.data[key] = value

    def get_data(self):
        return msgpack.packb(self.data)

    def load_data(self, packed_data):
        self.data = msgpack.unpackb(packed_data, raw=False)

    def read_int(self, key):
        return self.data.get(key)

    def read_uint(self, key):
        return self.data.get(key)

    def read_short(self, key):
        return self.data.get(key)

    def read_ushort(self, key):
        return self.data.get(key)

    def read_float(self, key):
        return self.data.get(key)

    def read_double(self, key):
        return self.data.get(key)

    def read_char(self, key):
        return self.data.get(key)

    def read_string(self, key):
        return self.data.get(key)