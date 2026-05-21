# Schéma `index.json` — modèles externes v1

## Structure minimale

```json
{
  "schema": "maths_espace_prof.modeles_externes.v1",
  "version": "2026-05-20",
  "modeles": [
    {
      "id": "identifiant_unique",
      "titre": "Titre du modèle",
      "type_document": "feuille_methode",
      "niveau": "Terminale spécialité",
      "chapitre": "Suites",
      "statut": "modele_valide",
      "priorite": "haute",
      "tags": ["sobre", "aéré"],
      "fichiers": [
        {
          "nom": "modele.tex",
          "type": "tex",
          "role": "source_latex",
          "url": "https://raw.githubusercontent.com/TON_COMPTE/modeles-maths-publics/main/modeles/.../modele.tex"
        }
      ],
      "notes_style": "Ce qu'il faut imiter.",
      "regles_ia": ["Règle 1", "Règle 2"],
      "vigilances": ["Point à vérifier"]
    }
  ]
}
```

## Champs recommandés

- `id` : identifiant stable, sans accents ni espaces.
- `titre` : titre lisible.
- `type_document` : type de production.
- `niveau` : niveau scolaire.
- `chapitre` : chapitre principal.
- `statut` : `modele_valide`, `reference_style`, `candidat_modele`, etc.
- `priorite` : `haute`, `moyenne`, `basse`.
- `tags` : mots-clés courts.
- `fichiers` : liens publics vers les fichiers.
- `notes_style` : ce que l’IA doit imiter.
- `regles_ia` : règles impératives.
- `vigilances` : pièges ou interdictions.
