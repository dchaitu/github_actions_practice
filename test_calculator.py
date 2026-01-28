import pytest
import yaml
from calculator import add, subtract, multiply, divide

def load_test_data():
    with open("test_data.yaml", "r") as f:
        data = yaml.safe_load(f)
    return data["tests"]

@pytest.mark.parametrize("test_case", load_test_data())
def test_calculator(test_case):
    a = test_case["a"]
    b = test_case["b"]
    operation = test_case["operation"]
    expected = test_case["expected"]

    if operation == "add":
        assert add(a, b) == expected
    elif operation == "subtract":
        assert subtract(a, b) == expected
    elif operation == "multiply":
        assert multiply(a, b) == expected
    elif operation == "divide":
        assert divide(a, b) == expected
    else:
        pytest.fail(f"Unknown operation: {operation}")
