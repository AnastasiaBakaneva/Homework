import pytest
from app.calc import Calculator

class Test_Positiv_test:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):    # Позитивный тест на умножение
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division(self):    # Позитивный тест на деление
        assert self.calc.division(self, 25, 5) == 5

    def test_subtraction(self):    # Позитивный тест на вычитание
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding(self):    # Позитивный тест на сложение
        assert self.calc.adding(self, 10, 6) == 16