"""
Pour cette partie nous allons reprendre le programme précédent mais on va légèrement le compléter.
"""
# --< Import des variables d'environnement >-- #
import smbus
import time

# --< Programme principal >-- #
smbus = smbus.SMBus(1)
adress = 0x48

# ici on définis une fonction pour chaque capteur : 
def photo():
    value = smbus.read(adress, 1, 10) 
    return value;

def therm():
    value = smbus.read(adress, 0, 10) 
    return value;

def potentio():
    value = smbus.read(adress, 3, 10) 
    return value;

# et on reprend le principe utilisé dans l'expérience sur la led
try:
    while 1 :
        print("Photoresistance : ", photo())
        print("Thermistance : ", therm())
        print("Potentiomètre : ", potentio())
        
        # on peut abréger cette ligne en utilisant un seul print() (print(Photoreistance : photo() \n Thermistance :  therm() \n Potentiomètre :  potentio()))
        # ou encore print(Photoreistance : %i \n Thermistance : %i\n Potentiomètre :  %i \n\n" % (photo(), therm(), potentio()))
        time.sleep(1) # on peut réduire la valeur ici mais il faut penser à l'utiliter que ça aurais et à l'impacte en terme de puissance que ça aurais sur le processeur
except KeyboardInterrupt: 
    pass   


"""
Les fonction renvoient une liste de valeurs, on peut donc en appeler une en particulier. 

Si des questions sur les suites subsistent cf "Les bases de python"/"les suites.py"
"""