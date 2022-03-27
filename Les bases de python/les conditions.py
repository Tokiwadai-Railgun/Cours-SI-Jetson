"""
Les conditions (même si pas tout le temps sous cette forme) sont au coeur des programmes il faut donc apprendre à bien les utiliser.

premièrement, comme pour toutes les autres instructions, il faut voir la syntaxe de la condition.

type (variablea "connecteur" variableb)):
    code
    
On remarque ici 3 élements de syntaxe:
le type : qui définis quand la condition est testée,
le connecteur : qui définis comment on teste
et les variables : qui sont les valeurs à comparer.


-- les types de conditions --
Globalement on a trois types de conditions:
- if : si
- elif : sinon-si
- else : sinon

Le if est la première condition, elif et else sont des conditions supplémentaires : 
en français ça donnerais : "si" ça égale ça alors ça "sinon-si" ça alors ça 

-- les connecteurs --
Il a 6 connecteurs : 
<= --> inférieur ou égal
< --> inférieur
>=  --> supérieur ou égal
> --> supérieur
== --> égal
!= --> différent

-- les variables --
C'est ici que prend tout l'intéret des variables booléennes, on vérifie si la condition est vraie ou fausse et on execute du code en fonction.
"""

# la théorié étant ce qu'elle est on passe à la pratique

# ici on va créer un programme qui va nous permettre de dire si un utilisateur est majeure ou non

# -- setup des variables --
ageMajeur = 10
ageUtilisateur = 10


# -- conditions --
if (ageUtilisateur >= ageMajeur):
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
    
"""
petit entrainnement

essayer de faire en sorte que si l'utilisateur a entre 15 et 18 ans, il a le droit de rentrer dans la salle de sport (ou autre exemple si on veut)
"""