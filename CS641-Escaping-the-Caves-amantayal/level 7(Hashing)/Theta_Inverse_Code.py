#This code is written in sage and find the polynomial Q as discussed in the report.

P.<x,z> = PolynomialRing(GF(2),2,order = 'lex')
Il = ideal([1+x^5,1+z^8])
R.<x,z> = QuotientRing(P,P.ideal(Il))
poly = 1+x + x^4*z
Q = (1/poly)
Q +=1
print(Q)