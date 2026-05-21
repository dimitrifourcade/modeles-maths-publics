# Guide — dépôt GitHub de modèles publics

## 1. Créer le dépôt

Créer un dépôt GitHub public, par exemple :

```text
modeles-maths-publics
```

## 2. Envoyer les fichiers

Envoyer tout le contenu de cette archive à la racine du dépôt.

Sur GitHub, il est possible d’utiliser :

```text
Add file > Upload files
```

puis de glisser-déposer les fichiers.

## 3. Remplacer les URLs dans `index.json`

Dans `index.json`, remplacer :

```text
TON_COMPTE
```

par ton nom d’utilisateur GitHub.

Si tu changes le nom du dépôt, remplacer aussi :

```text
modeles-maths-publics
```

par le nom réel du dépôt.

## 4. Tester l’URL raw

L’URL principale doit ressembler à :

```text
https://raw.githubusercontent.com/TON_COMPTE/modeles-maths-publics/main/index.json
```

Elle doit afficher directement le JSON dans le navigateur.

## 5. Charger dans le site

Dans le site Maths Espace Prof :

```text
/modeles
```

coller l’URL raw du fichier `index.json`, puis charger la bibliothèque.

## 6. Ajouter un modèle ensuite

Méthode simple :

1. créer un dossier pour le modèle ;
2. déposer les fichiers `.tex`, `.pdf`, `.md`, etc. ;
3. copier une entrée existante dans `index.json` ;
4. adapter `id`, `titre`, `niveau`, `chapitre`, `fichiers`, `notes_style`, `regles_ia`, `vigilances` ;
5. commit.

## 7. Bonnes pratiques

- Garder des noms de fichiers courts, sans accents, sans espaces.
- Préférer des chemins stables.
- Mettre les PDF lourds ailleurs si besoin.
- Toujours conserver le `.tex` quand il existe : c’est souvent le fichier le plus utile pour l’IA.
