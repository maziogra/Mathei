import sympy as sp;
from createSign import createSign;

x = sp.symbols('x')
f = sp.cos(x +3)*sp.log(x) + sp.sin(x)
signs = []
createSign(f, x, signs)
