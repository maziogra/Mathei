from fastapi import APIRouter
from core.Routes import (
    domainRoute,
    intersectionsRoute,
    symmetriesRoute,
    derivativesRoute,
    signRoute,
    asymptotesRoute,
    minMaxRoute
)
router = APIRouter()

router.include_router(domainRoute.router)
router.include_router(intersectionsRoute.router)
router.include_router(symmetriesRoute.router)
router.include_router(derivativesRoute.router)
router.include_router(signRoute.router)
router.include_router(minMaxRoute.router)
router.include_router(asymptotesRoute.router)