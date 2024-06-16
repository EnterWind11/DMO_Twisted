from enum import Enum

class PacketID(Enum):
    LOGIN = 0xffff
    SERVER_SELECTION = 0x0ce5
    CHARA_SELECTION = 0x06a5
    CONFIRM = 0x06a6
