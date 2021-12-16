from enum import Enum

class Status(Enum):
    WAIT    = 0
    REQ_BUY = 1
    BUY     = 2
    REQ_SELL= 3
    SELL    = 4