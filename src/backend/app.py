from src.backend.calculator import Calculator


class App:
    def __init__(self):
        print("Initialized")

    def calculate(self, num1: int, num2: int) -> int:
        # comment
        return Calculator().multiply(num1, num2)
