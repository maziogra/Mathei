import sympy as sp
from explainDerivatives import explainDerivatives

x = sp.symbols('x')
f = sp.log(x**2 + 1) * sp.sin(x) / (x + 1)
derivative = explainDerivatives(f, x)
print("Derivata : f'(x) = ", derivative)