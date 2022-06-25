from heys.diffSearch import *

alpha = [0x00, 0x01]
#       1    2       3       4       5         6
P = [1, 0.1, 0.0075, 0.001, 0.0002, 0.0001, 3.8e-06]
#P = [0.0001]*7
diffSearch(alpha, P, r = 6)

