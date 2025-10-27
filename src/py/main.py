import sympy as sp;
from segno import segno;

x = sp.symbols('x');
f = sp.sin(x)/sp.log(x) + sp.exp(x);
segno(f, x);