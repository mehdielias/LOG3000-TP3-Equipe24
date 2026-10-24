"""Tests de l'analyse et de l'évaluation des expressions (``app.calculate``).

Hypothèses (calculatrice arithmétique classique) :

* le format supporté est ``<nombre><opérateur><nombre>`` avec un seul opérateur ;
* les espaces sont ignorés et les décimaux (``.``) sont acceptés ;
* un opérande peut être négatif (``-5+3 == -2``) ;
* ``nan``/``inf`` ne sont pas des nombres saisissables sur une calculatrice ;
* toute entrée invalide lève ``ValueError`` ; la division par zéro lève
  ``ZeroDivisionError``.
"""

import pytest

from app import calculate


@pytest.mark.parametrize("expr, expected", [
    ("2+3", 5),
    ("10-4", 6),
    ("6*7", 42),
    ("9/3", 3),
    ("7/2", 3.5),
    ("3-10", -7),
    ("1.5+2.25", 3.75),
    ("0.5*4", 2),
])
def test_valid_expressions(expr, expected):
    """Les expressions bien formées donnent le résultat arithmétique attendu."""
    assert calculate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr, expected", [
    ("2 + 3", 5),
    ("  8 * 2  ", 16),
    ("1 0 + 5", 15),
])
def test_spaces_are_ignored(expr, expected):
    """Les espaces sont retirés avant l'analyse."""
    assert calculate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr, expected", [
    ("-5+3", -2),
    ("-2*4", -8),
    ("5*-3", -15),
    ("5--3", 8),
    ("4/-2", -2),
])
def test_negative_operands(expr, expected):
    """Un opérande négatif (signe ``-`` unaire) est accepté."""
    assert calculate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr", ["", None, 123, ["1+2"]])
def test_empty_or_non_string_input(expr):
    """Une entrée vide ou qui n'est pas une chaîne lève ``ValueError``."""
    with pytest.raises(ValueError):
        calculate(expr)


@pytest.mark.parametrize("expr", [
    "1+2+3",
    "1*2/3",
    "+",
    "5+",
    "*5",
    "12",
    "abc",
])
def test_malformed_expressions(expr):
    """Les expressions mal formées sont rejetées avec ``ValueError``."""
    with pytest.raises(ValueError):
        calculate(expr)


@pytest.mark.parametrize("expr", ["a+1", "1+b", "1.2.3+4", "1+--"])
def test_non_numeric_operands(expr):
    """Un opérande non numérique est rejeté avec ``ValueError``."""
    with pytest.raises(ValueError):
        calculate(expr)


@pytest.mark.parametrize("expr", ["nan+1", "inf-1", "1*infinity", "2+nan"])
def test_nan_and_inf_are_rejected(expr):
    """``nan`` et ``inf`` ne sont pas des nombres valides pour la calculatrice.

    ``float()`` les accepte, donc ils passent l'analyse actuelle.
    """
    with pytest.raises(ValueError):
        calculate(expr)


def test_division_by_zero():
    """Diviser par zéro lève ``ZeroDivisionError``."""
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")


def test_result_is_numeric():
    """Le résultat est un nombre (``int`` ou ``float``)."""
    assert isinstance(calculate("2+2"), (int, float))
