
KEY_LEN = 112
WORD_LEN = 4
BLOCK_LEN = WORD_LEN ** 2


# 12 var
#      0    1    2    3    4    5    6    7    8    9    A    B    C    D    E    F  
S =  [0x4, 0x5, 0x1, 0xC, 0x7, 0xE, 0x9, 0x2, 0xA, 0xF, 0xB, 0xD, 0x0, 0x8, 0x6, 0x3]
S_ = [0xC, 0x2, 0x7, 0xF, 0x0, 0x1, 0xE, 0x4, 0xD, 0x6, 0x8, 0xA, 0x3, 0xB, 0x5, 0x9]
# S_ = [0xC, 0x2, 0x7, 0xF, 0x0, 0x1, 0xE, 0x4, 0xD, 0x6, 0x8, 0xA, 0x3, 0xB, 0x5, 0x9]