from fastapi import HTTPException

class Number:
    @staticmethod
    def sum(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def divide(a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Não é permitido dividir por zero")
        return a / b

class Numbers:
    @staticmethod
    def sum(numbers_list: list[int]) -> int:
        total = 0
        for num in numbers_list:
            total = Number.sum(total, num)
        return total

    @staticmethod
    def average(numbers_list: list[int]) -> float:
        if not numbers_list:
            raise ValueError("Não é possível calcular a média de uma lista vazia")
        return sum(numbers_list) / len(numbers_list)