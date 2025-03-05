from app.models.math_models import Numbers

def sum_numbers(numbers: list[int]) -> int:
    return Numbers.sum(numbers)

def average_numbers(numbers: list[int]) -> float:
    return Numbers.average(numbers)