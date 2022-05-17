B = BooleanPolynomialRing(64, 'x', order='degrevlex')
B.inject_variables()

#f = x0 + x1 * x2*x3+ x4

f = x0 * x1 * x3 * x5 * x6 * x20 * x23 * x25 * x26 * x29 * x37 * x38 * x39 * x41 * x46 * x48 * x49 * x52 * x53 * x56 * x57 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x26 * x29 * x37 * x38 * x39 * x41 * x46 * x47 * x48 * x49 * x52 * x53 * x57 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x26 * x29 * x37 * x39 * x41 * x46 * x47 * x48 * x49 * x52 * x53 * x57 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x26 * x29 * x31 * x39 * x41 * x46 * x48 * x49 * x52 * x53 * x57 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x26 * x29 * x31 * x39 * x41 * x46 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x14 * x20 * x23 * x25 * x29 * x39 * x41 * x46 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x26 * x29 * x39 * x41 * x46 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x14 * x20 * x23 * x25 * x29 * x39 * x41 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x29 * x34 * x39 * x41 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x29 * x39 * x41 * x46 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x29 * x34 * x39 * x41 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x29 * x39 * x41 * x48 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x29 * x39 * x41 * x49 * x52 * x53 * x58 + x0 * x1 * x3 * x6 * x20 * x23 * x25 * x29 * x39 * x41 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x23 * x25 * x29 * x39 * x41 * x42 * x49 * x52 * x53 + x0 * x1 * x3 * x6 * x23 * x25 * x29 * x39 * x41 * x49 * x52 * x53 * x58 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x41 * x42 * x49 * x52 * x53 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x41 * x49 * x52 * x53 * x62 + x0 * x3 * x6 * x11 * x23 * x25 * x29 * x39 * x49 * x52 * x53 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x41 * x49 * x52 * x53 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x49 * x52 * x53 * x62 + x0 * x3 * x6 * x11 * x23 * x25 * x29 * x39 * x49 * x52 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x49 * x52 * x53 + x0 * x3 * x6 * x22 * x23 * x25 * x29 * x39 * x52 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x49 * x52 + x0 * x3 * x6 * x23 * x25 * x29 * x39 * x52 + x0 * x6 * x21 * x23 * x25 * x29 * x39 * x52 + x0 * x6 * x22 * x23 * x25 * x29 * x39 * x52 + x0 * x21 * x23 * x25 * x29 * x39 * x52 + x0 * x23 * x25 * x29 * x32 * x39 * x52 + x0 * x23 * x25 * x29 * x39 * x52 + x0 * x25 * x29 * x32 * x39 * x52 + x0 * x25 * x29 * x39 * x52 * x62 + x0 * x29 * x39 * x48 * x52 + x0 * x29 * x39 * x52 * x62 + x0 * x29 * x39 * x52 + x0 * x39 * x46 * x52 + x0 * x39 * x48 * x52 + x0 * x5 * x52 + x0 * x39 * x52 + x0 * x46 * x52 + x0 * x5 + x0 * x52 + x0 * x53 + x53 + 1
I = Ideal(f)
d = f.degree()

print("deg(f): "+str(d))

f1 = open('groebnerBasis_f1.txt')
f2 = open('groebnerBasis_f2.txt')

#for polynom in f1:
#    p = B(polynom)
#    print(p.degree())

#for polynom in f2:
#    p = B(polynom)
#    print(p.degree())

h1 = B(f1.readlines()[-1])
h2 = B(f2.readlines()[-1])
print("deg(h1):" + str(h1.degree()))
print("deg(h2):" + str(h2.degree()))



