from fastapi import HTTPException
import sympy as sp

def checkFunction(f, x):
    if f is None:
        raise HTTPException(status_code=400, detail="No function was provided")

    if f == sp.zoo:
        raise HTTPException(status_code=400, detail="Division by zero (zoo)")

    for i in f.free_symbols:
        if i != x:
            raise HTTPException(status_code=400, detail="Function is not correctly formatted")

    return f