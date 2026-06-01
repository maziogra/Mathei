import os

from fastapi import FastAPI
from core.Routes.routes import router as coreRouter
from account.Routes.routes import router as accountRouter
from FrontEnd.routes import router as frontendRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(coreRouter)
app.include_router(accountRouter)
app.include_router(frontendRouter)