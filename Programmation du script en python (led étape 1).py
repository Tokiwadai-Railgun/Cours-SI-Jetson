"""
grâce à ce programme nous allons faire en sorte que la led s'allume et s'éteigne, en soit qu'elle clignote

pour la structure du programme :
1- nous allons commencer par faire les imputs nessessaires

2- Puis nous allons ensuite initialiser les variables elles aussi nessessaires

3- ensuite nous allons faire en sorte que le programme s'arête si on appuis simultannément sur ctrl + c

4- et enfin nous allons faire en sorte que la led clignotte

(il faut noter que le nombre de commentaires et les nom des variables ne sont pas conformes aux "normes" d'écriture en python)
"""


# import des paquets nessessaires au fonctionnement du scipt
import Jetson.GPIO as GPIO
import time

# initialisatio nde svariables d'environnement et configurations des sorties
GPIO.setmode(GPIO.BOARD) # on dit au programme que l'on identifiras les pin de la carte via des chiffres
ledPin_output = 7 # pour pouvoir s'y retrouver après dans le script on met un chiffre dans une variable, ce chiffre correpondras au pin de la carte (la syntawe d'une variable est important, dans ce cas précis elle n'est pas respecté mais on y reviendras plus tard
GPIO.setup(ledPin_output, OUT) # ici on indique que le pin correspondant à la valeur de la variable (ici 7) seras une sortie (OUT)



# ici nous allons utiliser la fonction try | exept pour faire en sorte que la led clignote et que l'on puisse arêter le processus en appuiyant simplement sur une touche du clavier

try: # on essaie la boucle suivante ...
    # Boucle permettant d'allumer et d'éteindre la led à l'infinie 

    while 1:
        print("Led : ON")
        GPIO.output(ledPin_output, GPIO.HIGHT) # on définis la valeur du courant au pin "ledPin_output" étant "HIGHT", autement dit on envoie du courant là-bas

        time.sleep(2)

        print("Led : OFF")
        GPIO.output(ledPin_output, GPIO.LOW) # ici c'est l'inverse, le pin est définis sur "LOW" donc le courant n'y est plus envoyé

        time.sleep(2)

except KeyboardInterrupt: #  ... sauf si il y a une interruption clavier (ctrl +c), dans ce cas là on étein la lumière ...
    GPIO.output(ledPin_output, GPIO.LOW)
    GPIO.cleanup() # ... et on vide le cache de la carte
    print("Program : END")
    
    
    
    
 # -- Version sans commentaires explicatifs --

# import des paquets nessessaires au fonctionnement du scipt
import Jetson.GPIO as GPIO
import time

# --< initialisation des svariables d'environnement et configurations des sorties >-- #
GPIO.setmode(GPIO.BOARD) 
ledPin_output = 7 
GPIO.setup(ledPin_output, OUT) 

# programme principale
try:
    while 1:
        print("Led : ON")
        GPIO.output(ledPin_output, GPIO.HIGHT)

        time.sleep(2)

        print("Led : OFF")
        GPIO.output(ledPin_output, GPIO.LOW) 

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.output(ledPin_output, GPIO.LOW)
    GPIO.cleanup() 
    print("Program : END")
