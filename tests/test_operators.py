"""Tests unitaires des opérations de ``operators.py``.

Hypothèse : les fonctions doivent se comporter comme une calculatrice
arithmétique classique (``a + b``, ``a - b``, ``a * b``, ``a / b`` réels).
"""

import pytest

from operators import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, 3, 1),
    (0, 0, 0),
    (0.1, 0.2, pytest.approx(0.3)),
])
def test_add(a, b, expected):
    """L'addition renvoie la somme des deux opérandes."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 7),
    (3, 10, -7),
    (5, 5, 0),
    (0, 4, -4),
])
def test_subtract(a, b, expected):
    """La soustraction renvoie ``a - b`` (l'ordre des opérandes compte)."""
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (2, 0, 0),
    (-2, 5, -10),
    (2.5, 2, 5.0),
])
def test_multiply(a, b, expected):
    """La multiplication renvoie ``a * b`` (et non une exponentiation)."""
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (7, 2, 3.5),
    (-7, 2, -3.5),
    (1, 4, 0.25),
])
def test_divide(a, b, expected):
    """La division est réelle (``7 / 2 == 3.5``), pas une division entière."""
    assert divide(a, b) == expected


def test_divide_by_zero_raises():
    """Diviser par zéro lève ``ZeroDivisionError``."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
