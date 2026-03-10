# Prototipo
# https://gist.github.com/maziogra/fb4f5f1807a2e6dd6a9a72c858b81580

from fastapi import FastAPI
import sympy as sp
from Sign.createSign import createSign
from Domain.domain import domain # verificato
from Intercepts.intersections import intersections #verificato 
import Utils.findPeriod as findPeriod
from Symmetries.Symmetries import symmetries # veirificato
from Derivatives.explainDerivatives import explainDerivatives #verificato
app = FastAPI()

x = sp.symbols("x")
f = sp.sqrt(4-x**2) + 2*sp.asin(x/2)
intervals, signs = createSign(f, x)


@app.get("/domain")
async def get_domain(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        dominio = domain(expr, x)
        dominio = sp.pretty(dominio)
        
        return {
            "msg": "OK",
            "domain": str(dominio),
        }
    
@app.get("/intersections")
async def get_intersections(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        
        result = intersections(expr)
        
        punti = []
        for item in result:
            if not isinstance(item, str):
                punti.append(str(item))
            else:
                punti.append(item)
        
        return {
            "msg": "OK",
            "punti": punti,
        }
        
@app.get("/symmetries")
async def get_symmetries(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        
        simmetria = symmetries(expr)
        
        return {
            "msg": "OK",
            "symmetry": simmetria,
        }
        


@app.get("/derivatives")
async def get_derivatives(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        
        derivative = explainDerivatives(expr, x)
        
        return {
            "msg": "OK",
            "derivative": str(derivative),
        }
