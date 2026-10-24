# Flask Calculator

**LOG3000 – Travail pratique 3 – Équipe 24** (Polytechnique Montréal)

Calculatrice web simple construite avec Python et Flask.

## Équipe

| Membre | GitHub |
|--------|--------|
| Mehdi Nouadir | [@mehdielias](https://github.com/mehdielias) |
| _À compléter_ | _À compléter_ |

## But et portée du projet

L'application affiche une calculatrice dans le navigateur. L'utilisateur saisit
une opération avec les boutons, appuie sur `=`, et le **serveur Flask** évalue
l'expression et renvoie la page avec le résultat.

**Portée actuelle :**

- une seule opération par calcul, de la forme `nombre opérateur nombre`
  (ex. `12+5`, `7/2`) ;
- opérateurs : addition `+`, soustraction `-`, multiplication `*`, division `/` ;
- nombres décimaux acceptés (`1.5*2`) ;
- les erreurs (expression invalide, division par zéro…) sont affichées à
  l'écran sous la forme `Error: <message>`.

**Hors portée :** historique, parenthèses, enchaînement d'opérations
(`1+2+3`), fonctions scientifiques, comptes utilisateurs, base de données.

Le projet sert aussi de support à l'apprentissage des bonnes pratiques Git/GitHub
(issues, branches, pull requests) dans le cadre du cours LOG3000.

## Structure du dépôt

```
.
├── app.py                    # Serveur Flask, route "/" et analyse des expressions
├── operators.py              # Fonctions arithmétiques (add, subtract, multiply, divide)
├── templates/                # Page HTML (Jinja2)        -> templates/README.md
├── static/                   # Feuille de style CSS      -> static/README.md
├── tests/                    # Suite de tests pytest     -> tests/README.md
├── docs/                     # Résultats de tests et brouillons d'issues -> docs/README.md
├── requirements.txt          # Dépendances d'exécution (Flask)
├── requirements-dev.txt      # Dépendances de développement (Flask + pytest)
└── pytest.ini                # Configuration de pytest
```

## Prérequis

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/) 3.9 ou plus récent (développé avec 3.13)
- `pip` (livré avec Python)
- Un navigateur web

Vérifiez vos versions :

```bash
git --version
python --version
pip --version
```

## Installation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/mehdielias/LOG3000-TP3-Equipe24.git
   cd LOG3000-TP3-Equipe24
   ```

2. **Créer un environnement virtuel** (recommandé) :

   ```bash
   python -m venv .venv
   ```

3. **Activer l'environnement virtuel** :

   - Windows (PowerShell) : `.venv\Scripts\Activate.ps1`
   - Windows (Git Bash) : `source .venv/Scripts/activate`
   - macOS / Linux : `source .venv/bin/activate`

4. **Installer les dépendances** :

   ```bash
   pip install -r requirements-dev.txt
   ```

   (`requirements.txt` suffit si vous voulez seulement lancer l'application,
   sans les tests.)

## Utilisation

1. Depuis la racine du dépôt, avec l'environnement virtuel activé :

   ```bash
   python app.py
   ```

2. Ouvrez <http://127.0.0.1:5000/> dans votre navigateur.

3. Utilisez la calculatrice :
   - cliquez sur les chiffres et un opérateur pour composer l'opération (ex. `12`, `+`, `5`) ;
   - cliquez sur `=` pour obtenir le résultat ;
   - cliquez sur `C` pour vider l'écran.

4. Arrêtez le serveur avec `Ctrl+C`.

L'application est lancée en mode `debug` (rechargement automatique du code) :
**à ne pas utiliser en production**.

## Tests

Les tests utilisent [pytest](https://docs.pytest.org/). Depuis la racine du dépôt,
avec l'environnement virtuel activé et `requirements-dev.txt` installé :

```bash
python -m pytest            # toute la suite
python -m pytest -v         # sortie détaillée
python -m pytest -rf        # résumé des tests échoués
python -m pytest tests/test_operators.py   # un seul fichier
```

Voir [tests/README.md](tests/README.md) pour ce que couvre chaque fichier.

> **État actuel :** la base de code fournie contient des bogues connus ;
> une partie des tests échoue volontairement tant qu'ils ne sont pas corrigés
> (voir [docs/](docs/README.md) pour les résultats avant correction).

## Flux de contribution

1. **Issue d'abord** : chaque bogue ou fonctionnalité fait l'objet d'une
   [issue GitHub](https://github.com/mehdielias/LOG3000-TP3-Equipe24/issues) (description, comportement attendu/observé,
   étapes de reproduction) assignée à un membre de l'équipe.
2. **Une branche par issue**, créée depuis `main` et nommée de façon explicite,
   par exemple `fix/12-subtract-inverted-operands`.
3. **Corriger sur la branche**, relancer le test qui échouait ainsi que toute la
   suite : `python -m pytest`.
4. **Commits clairs** : un message qui explique *ce qui* est corrigé et
   *comment* (ex. `Corrige subtract: retourne a - b au lieu de b - a (#12)`).
5. **Pull Request** vers `main`, qui référence l'issue (`Closes #12`) et indique
   quels tests passent désormais. Ce dépôt est un *fork* : GitHub propose par
   défaut le dépôt d'origine comme cible. Vérifiez que le **base repository**
   est bien `mehdielias/LOG3000-TP3-Equipe24` et la base `main` (avec la CLI :
   `gh pr create --repo mehdielias/LOG3000-TP3-Equipe24 --base main`).
6. **Revue** par au moins un autre membre, puis fusion dans `main`.
7. Ne poussez pas directement sur `main`.

## Documentation par répertoire

- [templates/README.md](templates/README.md)
- [static/README.md](static/README.md)
- [tests/README.md](tests/README.md)
- [docs/README.md](docs/README.md)
