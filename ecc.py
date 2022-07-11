from pythonlibs.ellipticcurve import *

G = [4,20]
ec29 = EllipticCurve(29,G); 
print(ec29)
#y^2 = x^3 + 4x + 20 (mod 29)

pt = EllipticCurveElt(ec29,[2,6]); pt
#(2, 6)
print(f"7*pt: {7*pt}")
#(3, 28)
print(f"37*pt: {37*pt}")
#(Infinity, Infinity)
pt1 = 9*pt
pt1 - pt
#(15, 27)
print('{0:f}'.format(ec29)) # Full format
#'EllipticCurve(29, (4,20))'