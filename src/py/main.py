import sympy as sp
from Sign.createSign import createSign
from Domain import dominio
from Intercepts import intersezioni
#from Limits.limiti import limiti
#from Derivatives.explainDerivatives import explainDerivatives
from Domain.dominio import dominio
from Intercepts.intersezioni import intersezioni

x = sp.symbols('x')
f = (1+x)/(x**2 - 3*x + 1)
dominio(f)
intersezioni(f)