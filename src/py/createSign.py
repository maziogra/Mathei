import sympy as sp;
from addInfinite import addInfinite
from findNearestPeriod import findNearestPeriod;
from test import test
from trovaPuntiCritici import trovaPuntiCritici

def createSign(f, x, signs):
    #Toglie i possibili None dalla lista dei segni
    count = 0
    for i in signs:
        if i == None:
            signs.pop(count)
        count += 1  
    if sp.srepr(f).startswith('Mul'):
        for arg in f.args:
            trig_functions = arg.find(lambda u: isinstance(u, (sp.sin, sp.cos, sp.tan)))
            if trig_functions:
                signs.append(findNearestPeriod(arg, x, signs))

    # Analizza somme (Add)
    elif sp.srepr(f).startswith('Add'):
        for arg in f.args:
            createSign(arg, x, signs)  # ricorsione per ogni termine della somma

    # Analizza funzioni singole
    else:
        trig_functions = f.find(lambda u: isinstance(u, (sp.sin, sp.cos, sp.tan)))
        if trig_functions:
            signs.append(findNearestPeriod(f, x, signs))
        else:
            signs.append(trovaPuntiCritici(f, x))

    print("Final signs:")
    print(signs)
    
    interlvals = []
    for element in signs:
        for interval in element[0]:
            interlvals.append(interval)

    interlvals = sorted(interlvals)
    print("Combined intervals:", interlvals)
    
    # Aggiunge -oo e +oo agli intervalli se non sono presenti pi all'inizio e alla fine
    addInfinite(interlvals)
    
    finalsigns = []
    finalsigns, interlvals = test(interlvals, finalsigns, f, x)
    for i in range(len(finalsigns)):
            print(f"Intervallo {interlvals[i]} -> {interlvals[i+1]}: segno {finalsigns[i]}")
    print("Continua poi come la funzione goniometrica singola...")