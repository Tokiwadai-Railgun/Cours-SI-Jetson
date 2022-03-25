"""
Commençons par définir ce qu'est une variable et comment ça marche.

Une variable est un espace mémoire composé une valeur et un nom et d'un ID. On pourrait l'assimiler à une boite avec une étiquette rangée dans une certaine étagère.
Pour créer cette boitte on écris "ma_variable = valeur". ainsi on a une valeur qui est assigné à un nom, on peut donc ainsi la retrouver facilement.

Rentrons dans la partis technique : 
lors de la création d'une variable l'ordinateur va regarder dans la mémoire la valeur, récupérer son ID et l'attribuer au nom de la variable.
-- ça veut dire que plusieurs variable peuvent avoir le même ID ?
Oui, totalement. 

## -- > ceci est valable pour les valeurs allant de 0 à 255, au delas de cette limite chaque variable auras une ID différente.


Dans python comme dans tous les autres languages, les variables sont spéparés en 3 types majegurs :
- Les variables "numériques"
- Les chaines de caractères
- Les booléans

Pour rentrer plus précisément dans le premier type il est possible de les sépare en 2 sous catégories :
- Les int : nombre entiers relatifs
- Les float : nombre réels relatifs

L'avantage du python est que l'on a pas besoin (comme en C++ par exemple) de préciser le type de la variable (int, string, fload, bool etc...), l'ordinateur le déduit automatiquement.
Il peut également déduire un changement de type (int en float, float en int etc...) quand on en modifie le contenu.
La seule chose à faire est de bien indiquer la valeur.
étant donné que la valeur change en fonction du type de la variable le moyen d'indiquer la valeur change aussi, ainsi :
"""

chaine_de_caractere = "bonjour" # --> variable de type string
nombre_entier = 5 # --> variable de type int
nombre_reel = 5.5 # --> variable de type float
vraie_valeur = True # --> variable de type bool

"Pour changer la valeur d'une variable il suffit de lui donner une nouvelle valeur : "

chaine_de_caractere = "bonjour tout le monde"

"""
de cette manière le contenue de "chaine_de_caractere" est passé de "bonjour" à "bonjour tout le monde".
"""

"""
Vous avez du vous en rendre compte ici mais python est un language dit "sensible à la casse" c'est à dire que la moindre différence entre deux nom de variable les différencie ainsi, chaine_de_caractère est différent de chaine_de_caractere et de chaine_De_caractere.
"""