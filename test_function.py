import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (6, 5,  1),
    (7, 3, 4),
])
def test_substract_parametrize(a, b, expected):
    from function import substract_parametrize
    answer = substract_parametrize(a, b)
    assert answer == expected


def test_find_max():
    from function import find_max
    answer = find_max([400, 750, 500])
    expected = 750
    assert answer == expected


def test_find_min():
    from function import find_min
    answer = find_min([400, 750, 500])
    expected = 400
    assert answer == expected


@pytest.mark.parametrize("b, expected", [
    ('A', 'A'),
])
def test_output_letter(b, expected):
    from function import output_letter
    answer = output_letter('A')
    assert answer == expected
