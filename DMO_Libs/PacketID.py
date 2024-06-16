from enum import Enum

class PacketID(Enum):
    LOGIN = 65535
    SERVER_SELECTION = 3301
    CHARA_SELECTION = 1701
    CONFIRM = 1702
