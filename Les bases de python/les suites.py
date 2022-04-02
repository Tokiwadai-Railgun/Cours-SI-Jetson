"""
Parlons suites.

Pour commencer, une suite c'est quoi?

Une suite (aussi appelé table, array ou autre) c'est une liste de valeurs qui sont successives, une sorte de tableau mais en variable
elle se définie comme une variable (cf : les variables.py") sauf qu'au lieu de directement donner une ou plusieurs valeur (ce qui est l'objectif à terme) on les mets entre crochets

maitenant parlons de l'organisation d'une suite
Simplement chaque valeur est attribué à un chiffre (une étiquette) allant de 0 à n-1 (n étant le nombre de valeurs dans la suite)
"""

# def d'une table
suite = [1, 2, 3, 4, 5, "bonjour", 7, 8, 9, 10]

"""
maintenant c'est bien on a une suite mais comment on l'utilise ?

et bien on l'appel comme une variable sauf que l'on précise l'étiquette juste après entre crochets
"""

# pour afficher "bonjour" à partir de la suite "suite" il suffit donc de faire
print(suite[6])