from fastapi import FastAPI
from core.Routes.routes import router as coreRouter
from account.Routes.routes import router as accountRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
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