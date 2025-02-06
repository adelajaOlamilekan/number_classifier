from fastapi import APIRouter
import service
router = APIRouter()

@router.get("/api/classify-number")
def classify_number(number:str):
    classifier_response = service.classify_number(number)
    return classifier_response