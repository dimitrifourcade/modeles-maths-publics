# Audit complet v43 — énoncés + corrigés

## Périmètre

Audit effectué sur les 8 thèmes finaux du parcours de révision Première spécialité :

- `PDF/E` : énoncés finaux ;
- `PDF/C` : corrigés finaux ;
- `TEX` : sources LaTeX correspondantes ;
- vérification spécifique des questions d'algorithme, de la faisabilité sans calculatrice et des méthodes utilisées dans les corrigés.

## Méthode de contrôle

1. Scan textuel des `.tex` et des PDF extraits en texte pour repérer les signaux à risque :
   - `ln`, `log`, `arccos`, `arcsin`, `arctan` ;
   - `arrondi`, `valeur approchée`, `approx`, `≈` ;
   - demandes explicites liées à la calculatrice ;
   - mots-clés algorithmiques : `Python`, `while`, `for`, `return`, `seuil`, `renvoie`.
2. Relecture des sujets type bac dans chaque énoncé.
3. Relecture des corrections associées.
4. Vérification spécifique des points validés par l'utilisateur :
   - pas de formule de Huygens dans Variables aléatoires ;
   - somme géométrique sous la forme validée ;
   - questions d'algorithme sans simulation longue à la main ;
   - absence de logarithme pour résoudre les équations exponentielles ;
   - pas de calcul d'angle approché en produit scalaire.

## Bilan général

Verdict : **archive exploitable sans calculatrice**.

Les exercices finaux ne demandent pas de calculatrice. Les rares valeurs numériques longues qui apparaissent sont **données dans l'énoncé**, notamment dans le sujet de suites avec algorithme de seuil, et ne sont pas à produire par les élèves.

## Bilan par thème

| Thème | Énoncé | Corrigé | Verdict |
|---|---|---|---|
| Second degré | Calculs exacts, tableaux de signe/variations, pas d'approximation | Résolutions classiques par factorisation/discriminant | OK |
| Probabilités conditionnelles | Fractions et pourcentages simples, arbres/tableaux | Rédaction des probabilités totales correcte, calculs fractionnaires raisonnables | OK |
| Suites | Sommes géométriques, pourcentages, algorithme de seuil avec tableau fourni | Formule de somme géométrique sous la forme validée ; algorithme interprété sans simulation longue | OK |
| Dérivation | Études de fonctions et exponentielle en dérivée de référence | Pas de calculatrice ; comparaisons exactes avec inégalités admises | OK |
| Trigonométrie | Angles remarquables, valeurs exactes, pas d'approximation | Résolutions sur intervalles avec cercle trigonométrique | OK |
| Produit scalaire | Distances exactes, cosinus exacts, pas d'angle approché | Aucune utilisation d'arccos ; calculs exacts | OK |
| Variables aléatoires | Lois, espérance, variance par somme | Pas de Huygens ; variance calculée directement avec les écarts à l'espérance | OK |
| Exponentielle | Équations/inéquations résolues par égalité des exposants, monotonie ou changement de variable | Pas de logarithme ; pas de décimales imposées | OK |

## Points contrôlés en détail

### Algorithmes

Le point sensible était le document `Suites`. Le sujet de seuil utilise désormais un tableau fourni autour du seuil :

- l'élève ne doit pas exécuter toute la boucle à la main ;
- il lit le premier rang où la condition est réalisée ;
- il interprète la valeur renvoyée ;
- il modifie seulement la condition de boucle pour un autre seuil.

Verdict : **conforme sans calculatrice**.

### Somme géométrique

Forme validée présente dans la fiche et les corrigés :

```tex
u_0+u_1+\cdots+u_n = u_0\frac{1-q^{n+1}}{1-q}
```

La correction du sujet de suites utilise bien cette orientation :

```tex
u_0+\cdots+u_4 = 200\times\frac{1-0,9^5}{1-0,9}
```

Verdict : **conforme**.

### Variables aléatoires

Les corrections calculent les variances directement sous la forme :

```tex
V(X)=\sum p_i(x_i-E(X))^2
```

Aucune formule de Huygens n'est utilisée dans les corrections finales. Le distracteur `E(X^2)` apparaît seulement comme proposition fausse dans un QCM, ce qui est acceptable.

Verdict : **conforme**.

### Exponentielle

Aucun logarithme n'est utilisé pour résoudre les équations ou inéquations. Les exercices reposent sur :

- comparaison d'exposants ;
- changement de variable `X=e^x` quand les racines sont compatibles ;
- signe de `e^x` ;
- croissance de l'exponentielle.

La mention `e≈2,718` apparaît uniquement comme rappel culturel dans la fiche, pas comme outil de calcul dans les exercices.

Verdict : **conforme**.

### Produit scalaire

Aucune question ne demande une mesure approchée d'angle. Les exercices s'arrêtent aux valeurs exactes de cosinus, aux produits scalaires, aux équations de droites/cerccles et aux distances exactes.

Verdict : **conforme**.

## Signaux repérés mais non bloquants

- `environ` dans la phrase de variables aléatoires : « Sur un grand nombre de parties, le gain moyen est d'environ E(X) euro par partie. »  
  Ce n'est pas une demande de calcul approché ; c'est une interprétation statistique de l'espérance.
- `e≈2,718` dans la fiche exponentielle.  
  Ce n'est pas utilisé dans les exercices ; il peut rester comme rappel de culture mathématique.
- Table de valeurs longue dans Suites sujet 3.  
  Les valeurs sont fournies : l'élève n'a pas à les produire.

## Conclusion

L'archive v43 est validée comme **audit complet énoncés + corrigés** pour la faisabilité sans calculatrice.

Aucune correction mathématique supplémentaire n'a été nécessaire après la v42. La v43 ajoute ce rapport complet à l'archive.
