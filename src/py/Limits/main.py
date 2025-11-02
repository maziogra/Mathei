import sympy as sp;
from limiti import limiti

x = sp.symbols('x')
f = sp.Pow((x+1), 1/x)

limiti(f, x, sp.oo)