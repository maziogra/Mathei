import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_PATH = os.path.join(BASE_DIR, '')

@router.get("/{full_path:path}")
async def serve_spa(full_path: str):
    file_path = os.path.join(FRONTEND_PATH, full_path)
    if os.path.exists(file_path) and not os.path.isdir(file_path):
        return FileResponse(file_path)
    return FileResponse(os.path.join(FRONTEND_PATH, "index.html"))