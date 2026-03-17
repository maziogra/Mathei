from fastapi import FastAPI
from Routes import domainRoute, intersectionsRoute, symmetriesRoute, derivativesRoute, signRoute

app = FastAPI()

app.include_router(domainRoute.router)
app.include_router(intersectionsRoute.router)
app.include_router(symmetriesRoute.router)
app.include_router(derivativesRoute.router)
app.include_router(signRoute.router)