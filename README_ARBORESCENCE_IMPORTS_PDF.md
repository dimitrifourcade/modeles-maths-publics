# Arborescence GitHub — modèles PDF importés

Cette archive sert à créer une structure propre dans le dépôt public `modeles-maths-publics`.

Objectif : pouvoir déposer rapidement des PDF ou fichiers associés dans `documents_a_classer/`, puis les retrouver, les analyser avec ChatGPT, et les référencer dans `index.json` lorsqu'ils doivent apparaître dans `/modeles`.

## Règle simple

Tous les documents déposés dans cette arborescence sont considérés comme des modèles ou références exploitables.  
La différence est seulement leur niveau de classement :

- `documents_a_classer/00_inbox_a_trier/` : dépôt rapide, sans réfléchir.
- `documents_a_classer/01_lycee/` : modèles lycée déjà rangés par niveau et type.
- `documents_a_classer/02_cpge/` : modèles CPGE.
- `documents_a_classer/03_grand_oral/` : modèles ou références pour le Grand Oral.
- `documents_a_classer/04_references_style/` : documents utiles surtout pour leur style.
- `documents_a_classer/90_modeles_a_referencer_index_json/` : modèles déjà retenus, à ajouter ensuite dans `index.json`.
- `documents_a_classer/91_rejetes_ou_obsoletes/` : documents à conserver comme trace mais à ne pas utiliser.
- `documents_a_classer/92_doublons_a_verifier/` : doublons ou versions proches à comparer.
- `documents_a_classer/99_exports_index_json/` : entrées JSON générées par le site pour alimenter `index.json`.

## Important pour GitHub

GitHub ne conserve pas les dossiers vides. Chaque dossier contient donc un fichier `.gitkeep` ou `README.md`.

## Nommage conseillé

Utiliser des noms courts, sans espaces ni accents :

```text
fm_point_fixe_tspe_v4.pdf
controle_c1_tspe_type_bac_enonce.pdf
beamer_correction_c1_tspe.pdf
reference_style_tableaux_variations_tikz.pdf
```
