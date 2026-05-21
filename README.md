# Modèles Maths Publics

Dépôt public destiné à stocker les modèles pédagogiques utilisés par le site **Maths Espace Prof**.

Le site lit le fichier central :

```text
index.json
```

Une fois ce dossier envoyé dans un dépôt GitHub public, l’URL à coller dans le site sera de la forme :

```text
https://raw.githubusercontent.com/TON_COMPTE/modeles-maths-publics/main/index.json
```

## Organisation conseillée

```text
modeles/
  feuilles_methodes/
  controles/
  fiches_revision/
  corrections_beamer/
  cpge/
scripts/
docs/
index.json
```

## Règles importantes

- Ne pas publier de données nominatives d’élèves.
- Éviter les gros fichiers : GitHub convient surtout aux `.tex`, `.md`, `.json` et petits PDF.
- Chaque modèle doit avoir un identifiant stable.
- Les liens utilisés par le site doivent être publics.

## Mise à jour rapide

1. Ajouter les fichiers du modèle dans le bon dossier.
2. Ajouter ou modifier l’entrée correspondante dans `index.json`.
3. Commit sur GitHub.
4. Recharger la page `/modeles` du site.

Voir aussi : `docs/GUIDE_GITHUB_MODELES.md`.
