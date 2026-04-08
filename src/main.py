from fastapi import FastAPI
from core.Routes.routes import router as coreRouter
from account.Routes.routes import router as accountRouter

app = FastAPI()

app.include_router(coreRouter)
app.include_router(accountRouter)