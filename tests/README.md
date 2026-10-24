# tests/

Suite de tests [pytest](https://docs.pytest.org/) de la calculatrice.

## Exécution

Depuis la **racine du dépôt**, avec l'environnement virtuel activé et
`pip install -r requirements-dev.txt` effectué :

```bash
python -m pytest              # toute la suite
python -m pytest -v           # un résultat par test
python -m pytest -rf          # résumé des échecs en fin de sortie
python -m pytest tests/test_calculate.py            # un fichier
python -m pytest -k "subtract"                      # tests dont le nom contient "subtract"
```

La configuration (`pytest.ini` à la racine) ajoute la racine du projet au chemin
d'import : lancez toujours `pytest` depuis la racine.
Aucun serveur n'a besoin d'être démarré : les routes sont testées avec le client
de test intégré à Flask.

## Fichiers et couverture

| Fichier | Ce qu'il teste |
|---------|----------------|
| `conftest.py` | Fixtures partagées : `client` (client de test Flask) et `post_expression` (soumet une expression et renvoie le texte affiché à l'écran). |
| `test_operators.py` | `operators.py` : `add`, `subtract`, `multiply`, `divide` (cas normaux, négatifs, décimaux, division par zéro). |
| `test_calculate.py` | `app.calculate` : expressions valides, espaces, décimaux, opérandes négatifs, entrées vides ou non-chaînes, expressions mal formées, opérandes non numériques, `nan`/`inf`, division par zéro. |
| `test_routes.py` | Route `/` : GET, POST valide/invalide, champ absent, division par zéro, 404, 405, et libellés des boutons de la page HTML. |

## Hypothèses sur le comportement attendu

Les résultats attendus sont ceux d'une calculatrice arithmétique classique :

- `a - b`, `a * b` et `a / b` (division **réelle** : `7/2 = 3.5`) ;
- un opérande peut être négatif (`-5+3 = -2`, `5*-3 = -15`) ;
- `nan` et `inf` ne sont pas des nombres valides à saisir ;
- une entrée invalide lève `ValueError`, une division par zéro lève
  `ZeroDivisionError` ; à l'écran, les deux s'affichent en `Error: ...` ;
- le **format d'affichage** (`5` ou `5.0`) n'est pas testé : on compare des valeurs numériques ;
- chaque bouton affiche le caractère qu'il saisit (`2` insère « 2 »), et les
  boutons `*` et `/` ont un libellé visible (le choix du symbole, `*`/`×`, `/`/`÷`, est libre).

## État actuel

Les 84 tests passent. La suite a d'abord révélé 33 échecs sur le code fourni
([`../docs/baseline_test_results.txt`](../docs/baseline_test_results.txt)) ;
le résultat après correction est dans
[`../docs/final_test_results.txt`](../docs/final_test_results.txt).
