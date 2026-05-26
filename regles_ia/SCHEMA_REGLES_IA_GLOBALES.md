# Schéma — règles IA globales

Champs principaux :

- `regles_globales_obligatoires`
- `redaction_mathematique`
- `mise_en_page`
- `tableaux_signes_variations`
- `probabilites`
- `suites_recurrences`
- `calculatrice_niveaux`
- `corrections_beamer`
- `types_documents`
- `niveaux`
- `checklist_finale`

La page `/generer-avec-modeles` charge d’abord la version GitHub si elle existe :

```text
https://raw.githubusercontent.com/dimitrifourcade/modeles-maths-publics/main/regles_ia/regles_ia_globales.json
```

Puis elle bascule sur la copie locale du site si le fichier GitHub n’est pas encore installé.
