
from fastapi import FastAPI
import sympy as sp
from Domain.domain import domain
from Intercepts.intersections import intersections
from Symmetries.Symmetries import symmetries
from Derivatives.explainDerivatives import explainDerivatives
from Sign.createSign import createSign

app = FastAPI()

@app.get("/domain")
async def get_domain(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols('x')
        #expr = sp.parse_expr(f, evaluate=True)
        expr = sp.parse_expr(f, evaluate=True) 
        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        dominio = sp.pretty(domain(expr,x))

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
        expr = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)

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
        expr = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)

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
        expr = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)

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
    
@app.get("/sign")
async def get_sign(f: str | None = None):
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
        
        signs, intervals = createSign(expr, x)
        
        signs_intervals = []
        for i in range(len(signs)):
            signs_intervals.append((str(intervals[i]), str(intervals[i+1]), signs[i]))
        
        return {
            "msg": "OK",
            "signs_intervals": signs_intervals,
        }