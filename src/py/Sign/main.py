import sympy as sp;
from createSign import createSign;

x = sp.symbols('x')
f = sp.log(x) - x
createSign(f, x)