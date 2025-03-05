import pytest
from app.services.math_service import sum_numbers, average_numbers

def test_sum_numbers():
    result = sum_numbers([1, 2, 3, 4, 5])
    assert result == 15, f"Esperado 15, mas obteve {result}"

def test_average_numbers():
    result = average_numbers([1, 2, 3, 4, 5])
    assert result == 3.0, f"Esperado 3.0, mas obteve {result}"

def test_average_numbers_empty_list():
    with pytest.raises(ValueError):
        average_numbers([])