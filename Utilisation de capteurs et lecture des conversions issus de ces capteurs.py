# Pour plus de lisibilité il est possible de copier ce fichier sur VSCode et d'appuyer sur alt + Z pour éviter d'avoir à scroll sur le côté.

""" 
Question matériel, rapidement nous allons parler de pourquoi est-ce que l'on doit utiliser un module externe au Jetson Nano.

La raison est simple : Le Jetson Nano n'as pas de partie dédiée au traitement des informations fournis par des capteurs analogiques il faut donc en ajouter un, ce module serviras de "traducteur" au Jetson, il seras ainsi possible de lire des informations analogiques et d'en renvoyer.

(pour en savoir plus sur le fonctionnement de ce module, voir le site partie 2 vidéo "Expérience #3 : - Utiliser des capteurs analogiques via le port i2c" : https://www.sciences-ingenieur-f1.fr/premiere/sequence5/projet-sequence5/)
"""


"""
Avant de pouvoir passer à la partie programmation on va devoir installer de nouvelles dépendances à python pour pouvoir utiliser le port I2C.

--> sudo apt install python3-smbus
--> sudo apt install python-smbus

On peut désormais communiquer avec le module I2C.
Pour cela nous allons voir 3 programmes utilisant 3 modules intégrés à la carte.
"""

#pour connaître toutes les fonctionnalités de ce module, on peut aller sur le site : https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf
# à partir de la doc : récupérer l'adresse du composant I2C (page 13), /!\ il faut lire l'adresse en bits (en binaire) /!\ 
# Pour vraiment comprendre la doc cf vidéo

"""
Quel va être le but de ce premier programme ?

Simplement afficher dans le terminal la valeur image de la luminausité fournis par la photoresistance.
"""
# --< Import des variables d'environnement >-- #
import smbus
import time


# --< Programme principal >-- #
smbus = smbus.SMBus(1) # ici on définis le bus i2c à utiliser

adress = 0x48 # ici on définis l'adresse du composant I2C
value = smbus.read(adress, 1) # ici on lis la valeur de la photoresistance qu iest sur le port 1, le 10 indique que l'on veut lire 10 valeurs.

print(value)

# -< sans commentaires >- #
import smbus
import time


smbus = smbus.SMBus(1)

adress = 0x48
value = smbus.read(adress, 1) 

print(value)

"""
Deuxième programme :

Ici on affiche comme précedement une tension image mais cette fois-ci en utlisant la thermisance.
"""
# --< Import des variables d'environnement >-- #
import smbus
import time

# --< Programme principal >-- #
smbus = smbus.SMBus(1) # ici on définis le bus i2c à utiliser

adress = 0x48 # ici on définis l'adresse du composant I2C
value = smbus.read(adress, 2, 10) # ici on lis la valeur de la thermistance qui est donc sur le port 2

print(value)

# -< sans commentaires >- #
import smbus
import time

smbus = smbus.SMBus(1)

adress = 0x48
value = smbus.read(adress, 2, 10) 

print(value)

"""
Il est facilement remarquable que la seul chose qui change est la valeur de l'adresse du composant I2C, si on sais que le prochain module se trouve sur le port 3, il est donc facile de compléter le programme.

Comme il sagit d'un bon entrainnement si on a pas compris le fonctionnement ou la lecture de la doc il n'y auras pas d'exemple ici, il faut donc le faire soi même sur son Jetson.
"""


"""
Une fois tout aquis on peut passer à l'étape suivante qui se trouve dans le fichier "scrutation des capteurs.py"
"""