

# This file was *autogenerated* from the file gamma/gamma.sage
from sage.all_cmdline import *   # import sage library

_sage_const_64 = Integer(64); _sage_const_0 = Integer(0)
B = BooleanPolynomialRing(_sage_const_64 , 'x', order='degrevlex')
B.inject_variables()

fd = open("Variants_Gamma/V12.txt", "r") #read the gamma from file in mode read

gamma = list(fd.read())
#print(gamma)

p = B['x']('x^64 + x^63 + x^62 + x^60 + x^59 + x^58 + x^57 + x^56 + x^53 + x^50 + x^47 + x^45 + x^44 + x^43+ +x^42 +x^41 +x^40 +x^39 +x^38 +x^37 +x^36 +x^34 +x^32 +x^30 +x^28 +x^24 +x^18+ +x^15 +x^14 +x^13 +x^11 +x^9 +x^6 +x^4 + 1') #задаємо примітивний поліном зв. зв'язку
C = companion_matrix(p, format='bottom')
curr_state = vector(B, (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46, x47, x48, x49, x50, x51, x52, x53, x54, x55, x56, x57, x58, x59, x60, x61, x62, x63))
for i in range(_sage_const_0 ):
    curr_state = C * curr_state
    print()
    print(curr_state)
    print()





