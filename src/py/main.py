from fastapi import FastAPI
from Routes import domainRoute, intersectionsRoute, symmetriesRoute, derivativesRoute, signRoute, asymptotesRoute, minMaxRoute
from Utils.findNearestPeriod import findNearestPeriod
import sympy as sp

app = FastAPI()

app.include_router(domainRoute.router)
app.include_router(intersectionsRoute.router)
app.include_router(symmetriesRoute.router)
app.include_router(derivativesRoute.router)
app.include_router(signRoute.router)
app.include_router(minMaxRoute.router)
app.include_router(asymptotesRoute.router)