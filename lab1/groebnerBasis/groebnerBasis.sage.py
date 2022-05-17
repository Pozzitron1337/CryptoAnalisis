

# This file was *autogenerated* from the file groebnerBasis/groebnerBasis.sage
from sage.all_cmdline import *   # import sage library

_sage_const_64 = Integer(64); _sage_const_1 = Integer(1)
B = BooleanPolynomialRing(_sage_const_64 , 'x', order='degrevlex')
B.inject_variables()


f1 = x3 * x8 * x9 * x11 * x12 * x14 * x15 * x23 * x34 * x38 * x39 * x41 * x44 * x45 * x46 * x47 * x49 * x55 * x56 * x59 * x61 + x3 * x9 * x12 * x14 * x15 * x23 * x30 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x14 * x15 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x15 * x19 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x15 * x23 * x30 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x4 * x9 * x15 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x19 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x4 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 * x62 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x62 + x3 * x9 * x15 * x23 * x31 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 + x3 * x9 * x15 * x22 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x3 * x9 * x15 * x23 * x31 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x0 * x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x9 * x15 * x22 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x0 * x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x38 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x41 * x45 * x46 * x47 * x50 * x56 + x9 * x15 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x42 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x45 * x46 * x47 * x50 * x56 + x9 * x15 * x39 * x45 * x46 * x47 * x56 + x9 * x39 * x42 * x45 * x46 * x47 * x56 + x9 * x39 * x45 * x46 * x55 * x56 + x9 * x39 * x45 * x46 * x56 + x36 * x39 * x45 * x46 * x56 + x39 * x45 * x46 * x55 * x56 + x36 * x45 * x46 * x56 + x45 * x46 * x49 * x56 + x45 * x46 * x56 + x45 * x49 * x56 + x45 * x52 * x56 + x25 * x56 + x52 * x56 + x25 + x56
f2 = x3 * x8 * x9 * x11 * x12 * x14 * x15 * x23 * x34 * x38 * x39 * x41 * x44 * x45 * x46 * x47 * x49 * x55 * x56 * x59 * x61 + x3 * x9 * x12 * x14 * x15 * x23 * x30 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x14 * x15 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x15 * x19 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x12 * x15 * x23 * x30 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x4 * x9 * x15 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x19 * x23 * x34 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x4 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 * x62 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x59 + x3 * x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 * x62 + x3 * x9 * x15 * x23 * x31 * x39 * x41 * x45 * x46 * x47 * x49 * x55 * x56 + x3 * x9 * x15 * x22 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x3 * x9 * x15 * x23 * x31 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x0 * x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x9 * x15 * x22 * x23 * x39 * x41 * x45 * x46 * x47 * x49 * x56 + x0 * x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x23 * x38 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x23 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x38 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x41 * x45 * x46 * x47 * x50 * x56 + x9 * x15 * x39 * x41 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x42 * x45 * x46 * x47 * x56 + x9 * x15 * x39 * x45 * x46 * x47 * x50 * x56 + x9 * x15 * x39 * x45 * x46 * x47 * x56 + x9 * x39 * x42 * x45 * x46 * x47 * x56 + x9 * x39 * x45 * x46 * x55 * x56 + x9 * x39 * x45 * x46 * x56 + x36 * x39 * x45 * x46 * x56 + x39 * x45 * x46 * x55 * x56 + x36 * x45 * x46 * x56 + x45 * x46 * x49 * x56 + x45 * x46 * x56 + x45 * x49 * x56 + x45 * x52 * x56 + x25 * x56 + x52 * x56 + x25 + x56 + _sage_const_1 
I1 = Ideal(f1)
I2 = Ideal(f2)
GB1 = I1.groebner_basis()
GB2 = I2.groebner_basis()
fd1 = open("groebnerBasis_f1.txt", 'w')
fd2 = open("groebnerBasis_f2.txt", 'w')

for gb1 in GB1:
    fd1.write(str(gb1)+"\n")

for gb2 in GB2:
    fd2.write(str(gb2)+"\n")

