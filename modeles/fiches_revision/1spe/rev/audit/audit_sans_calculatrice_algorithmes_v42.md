# Audit v42 — Sans calculatrice et algorithmes

## Bilan

Archive relue avec deux angles :

1. faisabilité sans calculatrice ;
2. questions d'algorithme, en particulier dans le thème Suites.

## Correction appliquée

### Suites — Sujet 3 — Suite récurrente et seuil algorithmique

Dans la version précédente, la question demandait de déterminer ce que renvoyait l'algorithme. Le corrigé poursuivait alors une simulation numérique longue jusqu'au rang 11.

Correction v42 :

- l'énoncé fournit directement un petit tableau de valeurs autour du seuil ;
- l'élève doit interpréter le fonctionnement de l'algorithme et lire le rang dans le tableau ;
- le corrigé n'effectue plus une longue simulation à la main ;
- la question reste une vraie question d'algorithme : rôle de la boucle `while`, condition d'arrêt, rang renvoyé.

## Règle retenue

Un algorithme est compatible avec une épreuve sans calculatrice si l'élève doit comprendre, interpréter ou modifier le code, mais pas exécuter une longue boucle numérique à la main.

## Points de vigilance conservés

- Ne pas demander de calcul approché lourd.
- Ne pas demander de résolution par logarithme.
- Ne pas utiliser d'angle approché ou d'arccosinus numérique.
- Ne pas utiliser la formule de Huygens dans les corrections de variables aléatoires.
- Pour les sommes géométriques, utiliser la forme :

\[
u_0+u_1+\cdots+u_n=u_0\frac{1-q^{n+1}}{1-q}\qquad(q\neq1).
\]
