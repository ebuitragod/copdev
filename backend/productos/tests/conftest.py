#Bibliograf'ia https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input