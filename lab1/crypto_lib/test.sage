from nbformat import current_nbformat


B = BooleanPolynomialRing(64, 'x', order='degrevlex')
B.inject_variables()

fd = open("../Variants_Gamma/V12.txt", "r") #read the gamma from file in mode read
gamma = list(fd.read())

f = x3 * x8 * x9 * x11 * x12 * x14 * x15 * x23 * x34 * x38 * x39 * x41 * x44 * x45 * x46 * x47 * x49 * x55 * x56 * x59 * x61 + x3 * x9 * x12 * x14 * x15 * x23 * x30 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x14 * x15 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x15 * x19 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x15 * x23 * x30 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x4 * x9 * x15 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x19 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x4 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 * x62 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x62 + x3 * x9 * x15 * x23 * x31 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 + x3 * x9 * x15 * x22 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x3 * x9 * x15 * x23 * x31 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x0 * x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x9 * x15 * x22 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x0 * x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x38 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x41 * x45 * x46 * x47 * x50 * x56 + x9 * x15 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x42 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x45 * x46 * x47 * x50 * x56 + x9 * x15 * x39 * x45 * x46 * x47 * x56 + x9 * x39 * x42 * x45 * x46 * x47 * x56 + x9 * x39 * x45 * x46 * x55 * x56 + x9 * x39 * x45 * x46 * x56 + x36 * x39 * x45 * x46 * x56 + x39 * x45 * x46 * x55 * x56 + x36 * x45 * x46 * x56 + x45 * x46 * x49 * x56 + x45 * x46 * x56 + x45 * x49 * x56 + x45 * x52 * x56 + x25 * x56 + x52 * x56 + x25 + x56
p = B['x']('x^64 + x^63 + x^62 + x^60 + x^59 + x^58 + x^57 + x^56 + x^53 + x^50 + x^47 + x^45 + x^44 + x^43+ +x^42 +x^41 +x^40 +x^39 +x^38 +x^37 +x^36 +x^34 +x^32 +x^30 +x^28 +x^24 +x^18+ +x^15 +x^14 +x^13 +x^11 +x^9 +x^6 +x^4 + 1') #?????????????? ?????????????????????? ?????????????? ????. ????'????????
C = companion_matrix(p, format='bottom')

lines = None
with open("res_GB.txt", 'r') as file:
    lines = file.readlines()
    
curr_st = vector([1 if '+' in i else 0 for i in lines])

print(curr_st)

res = []
for i in range(500):
    curr_st = (C * curr_st)
    res.append(f(*curr_st))
    

res = [str(i) for i in res]
print(''.join(res))