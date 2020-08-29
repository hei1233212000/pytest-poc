import pytest
from util.util_functions import summation


def test_summation():
    a = 2
    b = 3
    result = summation(a, b)
    expected_result = a + b
    assert result == expected_result


@pytest.mark.parametrize("a,b,expected_result", [(3, 5, 8), (6, 9, 42), (2, 4, 6)])
def test_summation_by_using_parameterized_test(a, b, expected_result):
    result = summation(a, b)
    assert result == expected_result


@pytest.fixture()
def data_for_test():
    return [1, 2, 3]


def test_summation_by_using_fixture(data_for_test):
    print("\ndata_for_test: {}\n".format(data_for_test))
    a = data_for_test[0]
    b = data_for_test[1]
    expected_result = data_for_test[2]
    result = summation(a, b)
    assert result == expected_result
