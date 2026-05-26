# Installation — extraction automatique des archives ZIP

Cette mise à jour permet de traiter une archive ZIP presque comme un PDF isolé.

## À uploader dans GitHub

Uploader le contenu de cette archive à la racine du dépôt `modeles-maths-publics` :

```text
.github/workflows/extract_archives.yml
scripts/extract_archives.py
index_archives_extraites.json
documents_extraits_archives/README.md
```

Puis faire **Commit changes**.

## Utilisation

1. Déposer une archive `.zip` dans `documents_a_classer/` ou dans un sous-dossier.
2. Faire **Commit changes**.
3. Attendre que l’onglet **Actions** de GitHub termine le workflow `Extraire les archives de modèles`.
4. Vérifier que les fichiers apparaissent dans `documents_extraits_archives/`.
5. Revenir sur le site, page `/modeles-importes`, puis cliquer sur **Scanner les modèles**.

## Résultat attendu

Les PDF contenus dans l’archive disposent maintenant de vrais liens publics GitHub et peuvent être traités comme des PDF ordinaires par le site et par ChatGPT.
