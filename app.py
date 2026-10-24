"""Application web Flask : calculatrice à une opération.

Sert une page HTML (``templates/index.html``) dont le formulaire envoie
l'expression saisie (ex. ``"12+5"``) en POST ; le serveur l'évalue et
renvoie la même page avec le résultat (ou un message d'erreur) dans l'écran.
"""

import math

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Évalue une expression de la forme ``<nombre><opérateur><nombre>``.

    Les espaces sont ignorés. Exactement un opérateur parmi ``+ - * /`` est
    accepté, et les deux opérandes doivent être convertibles en ``float``.

    Args:
        expr: Expression à évaluer, par exemple ``"3 + 4.5"``.

    Returns:
        Le résultat de l'opération appliquée aux deux opérandes (``float``).

    Raises:
        ValueError: Si l'expression est vide ou n'est pas une chaîne, contient
            plus d'un opérateur, n'a pas la forme ``a op b`` ou si un opérande
            n'est pas un nombre fini (``nan`` et ``inf`` sont refusés).
        ZeroDivisionError: Si une division par zéro est demandée.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Route principale : affiche la calculatrice et traite le calcul.

    GET : renvoie la page avec un écran vide.
    POST : lit le champ de formulaire ``display``, appelle :func:`calculate`
    et renvoie la page avec le résultat. Toute exception est interceptée et
    affichée sous la forme ``"Error: <message>"`` afin de ne jamais renvoyer
    d'erreur HTTP 500 à l'utilisateur.

    Returns:
        Le HTML rendu de ``index.html`` avec la variable ``result``.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
