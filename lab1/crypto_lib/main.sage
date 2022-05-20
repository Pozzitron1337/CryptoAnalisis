B = BooleanPolynomialRing(64, 'x', order='degrevlex')
B.inject_variables()

fd = open("../Variants_Gamma/V12.txt", "r") #read the gamma from file in mode read
gamma = list(fd.read())

h1 = x56*x25 + x25
h2 = x56*x25 + x25 + x56 + 1

p = B['x']('x^64 + x^63 + x^62 + x^60 + x^59 + x^58 + x^57 + x^56 + x^53 + x^50 + x^47 + x^45 + x^44 + x^43+ +x^42 +x^41 +x^40 +x^39 +x^38 +x^37 +x^36 +x^34 +x^32 +x^30 +x^28 +x^24 +x^18+ +x^15 +x^14 +x^13 +x^11 +x^9 +x^6 +x^4 + 1') #задаємо примітивний поліном зв. зв'язку
C = companion_matrix(p, format='bottom')
curr_st = curr_state = vector(B, (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46, x47, x48, x49, x50, x51, x52, x53, x54, x55, x56, x57, x58, x59, x60, x61, x62, x63))

# print(h1(*(C^3 * curr_st)))

eqs = []

for i in range(500):
    curr_st = C * curr_st
    if gamma[i] == '0':
        eqs.append(h1(*(curr_st)))
    else:
        eqs.append(h2(*(curr_st)))
    
        

I = Ideal(eqs)
GB = I.groebner_basis()
fd = open("res_GB.txt", 'w')

for gb in GB:
    fd.write(str(gb)+"\n")