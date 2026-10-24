# Brouillons d'issues GitHub

Sept issues proposées, à créer après validation (aucune n'a encore été créée).
Chaque issue doit être assignée à un membre de l'équipe. Les commandes de test
se lancent depuis la racine du dépôt.

Légende : **Confirmé** = reproduit par un test qui échoue ; **À valider** =
dépend d'une hypothèse de comportement attendu.

---

## 1. `subtract` inverse les opérandes (`b - a` au lieu de `a - b`)

**Étiquettes proposées :** `bug`, `backend` — **Statut :** Confirmé

**Description :** la fonction `subtract` de `operators.py` retourne `b - a`.
Toute soustraction affiche donc l'opposé du résultat attendu.

**Comportement attendu :** `subtract(a, b) == a - b` ; `10-4` affiche `6`.

**Comportement observé :** `subtract(10, 3)` retourne `-7` ; `10-4` affiche `-6.0`.

**Reproduction :**
1. Lancer `python app.py` et ouvrir <http://127.0.0.1:5000/>.
2. Saisir `10`, `-`, `4`, puis `=`. L'écran affiche `-6.0` au lieu de `6.0`.

**Tests en échec :** `tests/test_operators.py::test_subtract[10-3-7]`, `[3-10--7]`, `[0-4--4]` ;
`tests/test_calculate.py::test_valid_expressions[10-4-6]`, `[3-10--7]` ;
`tests/test_routes.py::test_post_valid_expression[10-4-6]`.

**Piste de correction :** `return a - b`.

---

## 2. `multiply` calcule une puissance (`a ** b`) au lieu d'un produit

**Étiquettes proposées :** `bug`, `backend` — **Statut :** Confirmé

**Description :** `multiply` dans `operators.py` utilise l'opérateur `**`.

**Comportement attendu :** `multiply(a, b) == a * b` ; `6*7` affiche `42`.

**Comportement observé :** `multiply(3, 4)` retourne `81` ; `6*7` affiche
`279936.0` ; `2*0` donne `1`.

**Reproduction :**
1. Lancer l'application, saisir `6`, `*`, `7`, `=` (le bouton `*` n'a pas de
   libellé visible, voir issue 7).
2. Ou dans Python : `from operators import multiply; multiply(3, 4)` → `81`.

**Tests en échec :** `tests/test_operators.py::test_multiply[3-4-12]`, `[2-0-0]`, `[-2-5--10]`, `[2.5-2-5.0]` ;
`tests/test_calculate.py::test_valid_expressions[6*7-42]`, `[0.5*4-2]`, `test_spaces_are_ignored[  8 * 2  -16]` ;
`tests/test_routes.py::test_post_valid_expression[6*7-42]`.

**Piste de correction :** `return a * b`.

---

## 3. `divide` utilise la division entière (`//`) au lieu de la division réelle

**Étiquettes proposées :** `bug`, `backend` — **Statut :** Confirmé

**Description :** `divide` dans `operators.py` utilise `//` : le résultat est
arrondi vers le bas. Le message de la division par zéro mentionne aussi
« floor division ».

**Comportement attendu :** `divide(a, b) == a / b` ; `7/2` affiche `3.5`.

**Comportement observé :** `7/2` affiche `3.0` ; `1/4` donne `0.0` ; `-7/2`
donne `-4.0` ; `5/0` affiche `Error: float floor division by zero`.

**Reproduction :**
1. Lancer l'application, saisir `7`, `/`, `2`, `=` (le bouton `/` n'a pas de
   libellé visible, voir issue 7).
2. Ou dans Python : `from app import calculate; calculate("7/2")` → `3.0`.

**Tests en échec :** `tests/test_operators.py::test_divide[7-2-3.5]`, `[-7-2--3.5]`, `[1-4-0.25]` ;
`tests/test_calculate.py::test_valid_expressions[7/2-3.5]` ;
`tests/test_routes.py::test_post_valid_expression[7/2-3.5]`.

**Piste de correction :** `return a / b`.

---

## 4. Les nombres négatifs ne sont pas supportés

**Étiquettes proposées :** `bug`, `backend` — **Statut :** À valider (hypothèse : une calculatrice classique accepte `-5+3`)

**Description :** `calculate` (`app.py`) compte chaque `-` comme un opérateur et
rejette l'expression dès qu'un opérateur est en première position ou qu'il y en
a deux. Un nombre négatif est donc impossible à saisir ou à calculer, alors
que le bouton `-` est disponible en début d'expression.

**Comportement attendu :** `-5+3` → `-2` ; `5*-3` → `-15` ; `5--3` → `8` ; `4/-2` → `-2`.

**Comportement observé :** `-5+3` et `5*-3` lèvent `ValueError: only one operator is allowed` ;
l'écran affiche `Error: only one operator is allowed`.

**Reproduction :**
1. Lancer l'application, saisir `-`, `5`, `+`, `3`, `=`.
2. Ou : `from app import calculate; calculate("-5+3")`.

**Tests en échec :** `tests/test_calculate.py::test_negative_operands[...]` (5 cas) ;
`tests/test_routes.py::test_post_negative_operand`.

**Piste de correction :** accepter un signe `-` unaire au début de l'expression
et juste après l'opérateur.

---

## 5. `nan` et `inf` sont acceptés comme opérandes

**Étiquettes proposées :** `bug`, `backend`, `validation` — **Statut :** À valider

**Description :** `calculate` convertit les opérandes avec `float()`, qui accepte
`nan`, `inf` et `infinity`. Ces mots, non saisissables avec les boutons mais
postables directement à la route `/`, produisent un résultat au lieu d'une erreur.

**Comportement attendu :** `ValueError("operands must be numbers")`, affiché
`Error: operands must be numbers`.

**Comportement observé :** `calculate("nan+1")` retourne `nan` ; `calculate("2+nan")`
retourne `nan` ; `calculate("1*infinity")` retourne `inf`.

**Reproduction :**
1. `curl -X POST -d "display=nan+1" http://127.0.0.1:5000/` : l'écran affiche `nan`.
2. Ou : `from app import calculate; calculate("nan+1")`.

**Tests en échec :** `tests/test_calculate.py::test_nan_and_inf_are_rejected[nan+1]`,
`[inf-1]`, `[1*infinity]`, `[2+nan]`.

**Piste de correction :** n'accepter que des opérandes composés de chiffres et
d'un point décimal (regex ou `math.isfinite` après conversion).

---

## 6. Libellés incorrects des boutons `2` et `8` (« 02 » et « 88 »)

**Étiquettes proposées :** `bug`, `frontend` — **Statut :** Confirmé

**Description :** dans `templates/index.html`, le bouton qui insère `2` affiche
« 02 » et celui qui insère `8` affiche « 88 ». Seul l'affichage est faux : la
valeur insérée reste correcte.

**Comportement attendu :** les boutons affichent `2` et `8`.

**Comportement observé :** les boutons affichent `02` et `88`.

**Reproduction :** ouvrir <http://127.0.0.1:5000/> et regarder la 1re ligne
(bouton « 02 ») et la 3e ligne (bouton « 88 ») du pavé.

**Tests en échec :** `tests/test_routes.py::test_digit_button_label_matches_value[2]` et `[8]`.

**Piste de correction :** remplacer les libellés par `2` et `8`.

---

## 7. Les boutons `*` et `/` n'ont aucun libellé visible

**Étiquettes proposées :** `bug`, `frontend` — **Statut :** Confirmé

**Description :** dans `templates/index.html`, les boutons de multiplication
(`appendToDisplay('*')`) et de division (`appendToDisplay('/')`) ont un contenu
vide : on voit deux boutons orange sans symbole, ce qui rend ces opérations
inutilisables à la souris sans connaître leur position.

**Comportement attendu :** un symbole visible (`*` ou `×` ; `/` ou `÷`).

**Comportement observé :** libellés vides.

**Reproduction :** ouvrir <http://127.0.0.1:5000/> : la 3e ligne et la 4e ligne
du pavé (colonne de droite) sont des boutons orange vides.

**Tests en échec :** `tests/test_routes.py::test_operator_buttons_have_visible_label[*]` et `[/]`.

**Piste de correction :** ajouter le libellé entre les balises `<button>`.

---

## Correspondance tests ↔ issues

| Issue | Tests en échec (cas) |
|-------|----------------------|
| 1. subtract | 3 + 2 + 1 = 6 |
| 2. multiply | 4 + 3 + 1 = 8 |
| 3. divide | 3 + 1 + 1 = 5 |
| 4. nombres négatifs | 5 + 1 = 6 |
| 5. nan / inf | 4 |
| 6. libellés 2 et 8 | 2 |
| 7. libellés `*` et `/` | 2 |
| **Total** | **33** |
