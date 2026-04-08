from fastapi import APIRouter
from account.Routes import (
    loginRoute,
    registrationRoute
)
router = APIRouter()

router.include_router(loginRoute.router)
router.include_router(registrationRoute.router)