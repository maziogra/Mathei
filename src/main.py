import os

from fastapi import FastAPI
from core.Routes.routes import router as coreRouter
from account.Routes.routes import router as accountRouter
from FrontEnd.routes import router as frontendRouter

app = FastAPI()

app.include_router(coreRouter)
app.include_router(accountRouter)
app.include_router(frontendRouter)