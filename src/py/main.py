from fastapi import FastAPI
import sympy as sp
from segno.segno import segno

app = FastAPI()

@app.get("/sign")
async def sign(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        # Controlla se è stata inserita un altra "lettera" apparte x
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        
        punti, segni = segno(expr, x)

        # converte l'array da oggetti sympy a string
        for idx, i in enumerate(punti):
            if not isinstance(i, str):
                punti.pop(idx);
                punti.insert(idx, str(i))
                
        return {
                    "msg": "OK",
                    "punti": punti,
                    "segni": segni,
                }