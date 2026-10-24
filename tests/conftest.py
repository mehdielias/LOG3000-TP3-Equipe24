"""Fixtures partagées par la suite de tests."""

import re

import pytest

from app import app


@pytest.fixture
def client():
    """Client de test Flask (aucun serveur réel n'est démarré)."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def post_expression(client):
    """Renvoie une fonction qui soumet une expression au formulaire.

    La fonction retournée envoie ``expr`` dans le champ ``display`` (comme le
    fait le navigateur) et renvoie la valeur affichée à l'écran de la page
    résultante, sous forme de chaîne (résultat ou ``"Error: ..."``).
    """

    def _post(expr):
        response = client.post("/", data={"display": expr})
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        match = re.search(r'<input[^>]*id="display"[^>]*value="([^"]*)"', html)
        assert match, "champ #display introuvable dans la page"
        return match.group(1)

    return _post
