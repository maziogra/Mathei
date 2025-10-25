import sympy as sp;
from segno import segno;

x = sp.symbols('x');
f = sp.tan(x)*sp.sin(x);
segno(f, x);