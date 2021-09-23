# Interview Tech

## Formule de Luhn

La formule de Luhn est une formule de contrôle pour valider les numéros de carte de crédit (entre autre).

## Implémentation

La valeur en entrée est une chaine de charactère ne contenant que des chiffres valides.

1. La lecture du la chaine se fait de droite à gauche.
2. Les chiffres à une position pair (2ème chiffre, 4ème chiffre, etc...) sont doublés.
3. Si le chiffre doublé est suppérieur à `9`, on le remplace par la somme de ses chiffres.
    Par example `6` doublé devient `12` qui est suppérieur a `9` donc on fait `1+2 = 3`
4. On additionne tous les chiffres obtenu.
5. On vérifie que le total est un multiple de `10`, si c'est le cas la chaine est valide.

La valeur de sortie est un booléen.

## Example 1

Input: `0123465`

Etape 1:
`0123465` devient `0226435`, on a multiplié par 2 les chiffres `6`, `3` et `1`, le `6` étant devenu `12` donc `1 + 2` soit `3`.

Etape 2:
Chaque chiffre de `0226435` sont additionné pour donner `22`.

Etape 3:
`22` n'etant pas un multiple de `10` on retourne faux.

## Example 2

Input: `543215`

Etape 1:
`543215` devient `146225`

Etape 2:
Chaque chiffre de `146225` sont additionné pour donner `20`.

Etape 3:
`20` étant un multiple de `10` on retourne vrai.

## Exercice

Implémenter une classe qui permet de validé qu'un nombre est valide selon la formule de Luhn

## Question bonus

En réutilisant du code déjà écrit ajouter une méthode pour générer le chiffre de contrôle d'un numéro donné.

Par example:
- `012346` retourne `0123463`
- `54321` retourne `543215`
