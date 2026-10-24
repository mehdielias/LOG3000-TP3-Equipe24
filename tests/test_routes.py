"""Tests de la route Flask ``/`` et de la page HTML qu'elle sert."""

import re

import pytest


def test_get_index_returns_page(client):
    """GET / renvoie la page de la calculatrice avec un écran vide."""
    response = client.get("/")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Flask Calculator" in html
    assert re.search(r'id="display"[^>]*value=""', html)


def test_unknown_route_is_404(client):
    """Une route inexistante renvoie 404."""
    assert client.get("/inconnue").status_code == 404


def test_put_is_not_allowed(client):
    """Seules les méthodes GET et POST sont acceptées sur ``/``."""
    assert client.put("/").status_code == 405


@pytest.mark.parametrize("expr, expected", [
    ("2+3", 5),
    ("10-4", 6),
    ("6*7", 42),
    ("9/3", 3),
    ("7/2", 3.5),
])
def test_post_valid_expression(post_expression, expr, expected):
    """POST d'une expression valide affiche le bon résultat à l'écran.

    On compare la valeur numérique (``5`` ou ``5.0`` sont équivalents) :
    le format d'affichage n'est pas l'objet de ce test.
    """
    shown = post_expression(expr)
    assert not shown.startswith("Error"), shown
    assert float(shown) == pytest.approx(expected)


@pytest.mark.parametrize("expr", ["", "abc", "1+", "1+2+3", "a*b"])
def test_post_invalid_expression_shows_error(post_expression, expr):
    """Une expression invalide donne ``Error: ...`` sans erreur HTTP 500."""
    assert post_expression(expr).startswith("Error:")


def test_post_division_by_zero_shows_error(post_expression):
    """La division par zéro est affichée comme une erreur, pas un crash."""
    assert post_expression("5/0").startswith("Error:")


def test_post_without_display_field(client):
    """Un POST sans champ ``display`` est traité comme une expression vide."""
    response = client.post("/", data={})
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Error: empty expression" in html


def test_post_negative_operand(post_expression):
    """Le calcul avec un opérande négatif fonctionne via le formulaire."""
    shown = post_expression("-5+3")
    assert not shown.startswith("Error"), shown
    assert float(shown) == pytest.approx(-2)


def _buttons(html):
    """Extrait les boutons ``appendToDisplay`` de la page.

    Returns:
        Liste de tuples ``(valeur_envoyée, libellé_affiché)``.
    """
    return re.findall(
        r"onclick=\"appendToDisplay\('(.)'\)\">(.*?)</button>", html
    )


@pytest.mark.parametrize("digit", list("0123456789"))
def test_digit_button_label_matches_value(client, digit):
    """Le libellé de chaque bouton chiffre est le chiffre qu'il saisit."""
    buttons = dict(_buttons(client.get("/").get_data(as_text=True)))

    assert buttons[digit].strip() == digit


@pytest.mark.parametrize("operator", list("+-*/"))
def test_operator_buttons_have_visible_label(client, operator):
    """Chaque bouton d'opérateur affiche un libellé non vide."""
    buttons = dict(_buttons(client.get("/").get_data(as_text=True)))

    assert buttons[operator].strip() != ""
