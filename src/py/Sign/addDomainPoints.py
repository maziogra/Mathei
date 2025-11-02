import sympy as sp

def addDomainPoints(domain, punti):
    if isinstance(domain, sp.Union):
        for intervallo in domain   .args:
            for limite in [intervallo.start, intervallo.end]:
                if limite in punti:
                    continue
                if limite != sp.oo and limite != -sp.oo:
                    punti.append(limite)
    if isinstance(domain, sp.Interval):
        for limite in [domain.start, domain.end]:
            if limite in punti:
                    continue
            if limite != sp.oo and limite != -sp.oo:
                punti.append(limite)