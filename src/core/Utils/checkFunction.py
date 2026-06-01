from fastapi import HTTPException
import sympy as sp

def checkFunction(f, x):
    if f == None:
        raise HTTPException(status_code=400, detail="No function was provided")
    else:
        if str(f) == "zoo":
            raise HTTPException(status_code=400, detail="Division by zero")
        
        #for i in f.free_symbols:
         #   if i != x or i != sp.E or i != sp.pi:
          #      print("______________________________________________", i)
           #     raise HTTPException(status_code=400, detail="Function is not correctly formatted")
    
    return None