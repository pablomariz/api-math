from fastapi import APIRouter, HTTPException
from app.services.math_service import sum_numbers, average_numbers

router = APIRouter()

@router.post("/sum")
def sum_route(numbers: list[int]):
    return {"result": sum_numbers(numbers)}

@router.post("/average")
def average_route(numbers: list[int]):
    try:
        result = average_numbers(numbers)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
