# Autore: maziogra
# Refactoring: Shahid

import sympy as sp

def addDomainPoints(domain, punti):
    def add(p):
        if p not in punti and p not in [sp.oo, -sp.oo]:
            punti.append(p)

    if isinstance(domain, sp.Union):
        for elem in domain.args:

            if isinstance(elem, sp.Interval):
                for limite in [elem.start, elem.end]:
                    if limite is not None:
                        add(limite)

            elif isinstance(elem, sp.FiniteSet):
                for p in elem:
                    add(p)

    elif isinstance(domain, sp.Interval):
        for limite in [domain.start, domain.end]:
            if limite is not None:
                if domain.is_open:
                    add(limite)
                else:
                    add(limite)

    elif isinstance(domain, sp.FiniteSet):
        for p in domain:
            add(p)