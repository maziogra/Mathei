import sympy as sp;
from segno import segno;

x = sp.symbols('x');
f = sp.sin(x) * sp.tan(x);
segno(f, x);