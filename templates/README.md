# templates/

Gabarits HTML (Jinja2) rendus par Flask. Flask cherche automatiquement ce
dossier pour `render_template(...)`.

## Fichiers

| Fichier | Responsabilité |
|---------|----------------|
| `index.html` | Page unique de l'application : écran (`<input id="display">`), pavé de boutons et deux fonctions JavaScript (`appendToDisplay`, `clearDisplay`). |

## Fonctionnement

- Les boutons chiffres/opérateurs ajoutent leur caractère à l'écran **côté
  navigateur** (JavaScript) ; le bouton `=` soumet le formulaire en `POST`.
- Le serveur renvoie la même page, avec la variable Jinja `result`
  (résultat ou `Error: ...`) affichée dans l'écran.
- L'écran est en lecture seule : la saisie se fait uniquement avec les boutons.

## Dépendances et hypothèses

- Rendu par `app.py` (route `/`), qui fournit la variable `result`.
- Utilise `static/style.css` via `url_for('static', filename='style.css')`.
- Le nom du champ de formulaire (`display`) doit rester identique à celui lu
  dans `app.py` (`request.form.get('display')`).
- Fichier encodé en UTF-8.
