import os

from fastapi import UploadFile, File, APIRouter
from fastapi.responses import HTMLResponse
from PIL import Image
from munch import Munch
from pix2tex.cli import LatexOCR
import io

router = APIRouter()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, '..', '..', 'ModelConfig', 'config.yaml')
# Adjust the relative segments above to match your actual folder structure

args = Munch({
    'config': CONFIG_PATH,
    'checkpoint': os.path.join(BASE_DIR, '..', '..', 'ModelConfig', 'mixed_e30_step16834.pth'),
    'no_cuda': True,
    'no_resize': True
})

model = LatexOCR(args)

# API PREDICT
@router.post("/predict")
async def predict(image: UploadFile = File(...)):
 
    image_bytes = await image.read()
 
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
 
    result = model(img)
 
    return {"latex": result}