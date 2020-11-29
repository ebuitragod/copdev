import pytest
#run  pytest -k divisible -v

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0