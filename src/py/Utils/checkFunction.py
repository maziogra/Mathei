import sympy as sp

def checkFunction(f, x):
    if f == None:
        return {"msg": "No function was provided"}
    else:
        if str(f) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in f.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
    
    return None