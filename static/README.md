# static/

Ressources statiques servies telles quelles par Flask sous l'URL `/static/...`.

## Fichiers

| Fichier | Responsabilité |
|---------|----------------|
| `style.css` | Style de la calculatrice : centrage de la page, écran, grille de 4 colonnes pour les boutons, couleurs des touches (orange pour les opérateurs et `=`) et états `hover`/`active`. |

## Dépendances et hypothèses

- Référencé par `templates/index.html` via `url_for('static', filename='style.css')`.
- Les sélecteurs dépendent des identifiants et classes du HTML : `#display`,
  `.calculator`, `.buttons`, `.btn`, `.operator`. Renommer l'un de ces éléments
  dans le HTML exige de mettre à jour ce fichier.
