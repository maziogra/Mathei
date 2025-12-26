import sympy as sp;

#controllo esponent c.e.
def dominio(funzione):
   x=sp.symbols("x")
   dominio=sp.S.Reals
   denominatore=sp.denom(sp.together(funzione))
   # ho una frazione tolgo gli zeri, poi c.e nel for per tutte
   if denominatore !=1:
      zeridiDenom=sp.solveset(sp.Eq(denominatore,0),x, sp.S.Reals)
      dominio=dominio-zeridiDenom

   # analizzo la funzione dove ogni funxione( anche le compste) e un nodo di un albero
   # di ogni 'nodo' calcolo dominio poi interseco tutto
   for fun in sp.preorder_traversal(funzione):
         #esponenzial
         if isinstance(fun,sp.Pow):
            base= fun.args[0]
            esponente=fun.args[1]
            if esponente.is_Rational and (esponente.q % 2==0):
                ce=sp.solveset(sp.Ge(base,0),x,dominio)
                dominio=dominio.intersect(ce)
         #logaritm
         if isinstance(fun,sp.log):
             argomento=fun.args[0]
             ce=sp.solveset(sp.Gt(argomento,0),x,dominio)
             dominio=dominio.intersect(ce)
         #gogn 
         k = sp.symbols('k', integer=True)
         if fun.func == sp.tan or fun.func == sp.sec:
            # periodo t mi da zero in caso di x^2 ecc e uno in caso di x, altimenti coef per cui è moltiplicata x
            t=abs(fun.args[0].coeff(x))
            #controllo
            if t==0 or t==1:
                esclusi = sp.ImageSet(sp.Lambda(k, sp.pi/2 + k*sp.pi), sp.S.Integers)
            else:
                esclusi = sp.ImageSet(sp.Lambda(k,(1/t)*sp.pi/2 +(1/t)* k*sp.pi), sp.S.Integers)
            dominio = dominio - esclusi

         elif fun.func == sp.cot or fun.func == sp.csc:
            t=abs(fun.args[0].coeff(x))  # modulo dato che non posso avere periodo negativo
            if t==0 or t==1:
               esclusi = sp.ImageSet(sp.Lambda(k, k*sp.pi), sp.S.Integers)
            else:
                esclusi = sp.ImageSet(sp.Lambda(k,(1/t)*k*sp.pi), sp.S.Integers)
            dominio = dominio - esclusi

         elif fun.func == sp.asin or fun.func == sp.acos:
            arg = fun.args[0]
            condizione = sp.And(arg >= -1, arg <= 1)
            soluzione = sp.solveset(condizione, x, dominio)
            dominio = dominio.intersect(soluzione)
   print("dominio:") 
   print(dominio)
   return dominio
               

