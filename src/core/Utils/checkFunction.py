from fastapi import HTTPException
import sympy as sp

def checkFunction(f, x):
    if f == None:
        raise HTTPException(status_code=400, detail="No function was provided")
    else:
        if "zoo" in str(f):
            raise HTTPException(status_code=400, detail="Division by zero")
        
        for i in f.free_symbols:
            if i != x:
                raise HTTPException(status_code=400, detail="Function is not correctly formatted")
    
    return None