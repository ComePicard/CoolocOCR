import base64

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models.receipt import Receipt
from app.services.ocr import extract_data_from_receipt

router = APIRouter()


@router.post("/extract_receipt/")
async def ocr_image(file: UploadFile = File(...)) -> Receipt:
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Le fichier doit être une image.")

    content = await file.read()
    b64_image = base64.b64encode(content).decode("utf-8")
    try:
        receipt = extract_data_from_receipt(b64_image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur OCR : {str(e)}")

    return receipt
