"""Opérations arithmétiques de base de la calculatrice.

Chaque fonction prend deux opérandes (a, b) et renvoie le résultat de
``a <opérateur> b``. Elles sont référencées par la table ``OPS`` de ``app.py``.
"""


def add(a, b):
    """Additionne deux nombres.

    Args:
        a: Premier opérande (``float`` ou ``int``).
        b: Second opérande.

    Returns:
        La somme ``a + b``.
    """
    return a + b


def subtract(a, b):
    """Soustrait le second opérande du premier.

    Args:
        a: Premier opérande (celui dont on soustrait).
        b: Second opérande (celui qui est soustrait).

    Returns:
        La différence attendue ``a - b``.
    """
    return a - b


def multiply(a, b):
    """Multiplie deux nombres.

    Args:
        a: Premier facteur.
        b: Second facteur.

    Returns:
        Le produit attendu ``a * b``.
    """
    return a * b


def divide(a, b):
    """Divise le premier opérande par le second.

    Args:
        a: Dividende.
        b: Diviseur.

    Returns:
        Le quotient réel attendu ``a / b``.

    Raises:
        ZeroDivisionError: Si ``b`` vaut 0.
    """
    return a / b
