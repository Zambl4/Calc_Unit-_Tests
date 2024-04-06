import pytest

from app.calc import Calculation

class TestCalc:

   def setup(self):
       self.calc = Calculation

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 3, 3) == 9

   def test_division_calculate_correctly(self):
       assert self.calc.division(self, 2, 2) == 1

   def test_subtraction_calculate_correctly(self):
       assert self.calc.subtraction(self, 2, 2) == 0

   def test_adding_calculate_correctly(self):
       assert self.calc.adding(self, 3, 3) == 6
