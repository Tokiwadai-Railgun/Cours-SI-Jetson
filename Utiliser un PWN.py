"""
--- introduction à l'utilisation de modules PWM ---
Utilisation d'un module PWM :

déjà à quoi ça sert? 
Le PWM sert à moduler la quantitée d'énergie envoyé à un composant, ici nous allons l'utiliser pour faire varier la luminositée de la led

commment on va proicéder?
et bien on va changer le pin, précedement on utilisais le pin 7, ici on utiliseras le 33. Pour parler en français,on va utiliser le "port usb pour module miniature" (nom non factuelle) n°33 et non n°7 car le n°33 possède l'option que l'on veut utiliser (PWM) 

"Éhe mais, c'est sympa de savoir que le pin 7 est de type GPIO et que le 33 est de type PWM mais concrètement comment on fait pour savoir de quel type est chaque pin" question logique avec une réponse simple :
il faut évidement regarder la documentation du Jetson Nano fournis par NVIDIA (https://developer.nvidia.com/embedded/community/support-resources)


"""

"""
--- Mise en places des choses nessessaires à utilisation des ports PWM ---

pour utiliser ces fameux ports magique nous permettant de moduler le courant que l'on envoie il faut commencer par inisitliser quelques scriptes avec le terminal

commandes:
sudo /opt/nvidia/jeston-io/jetson-io.py
"Configure Jetson 40pin Header"
"Configure header pins manually"
"pwm2" (33)
"Back"
"Save pin changes"
"Save and reboot to reconfigure pins"
"""

# une fois ceci terminé on peut commencé notre script dans un nouveau fichier python (ne pas oublier l'extention .py)

# -- import des dépendances
import Jetson.GPIO as GPIO
import time

# -- mise en place des variables et du setup nessessaire
output_pin = 33     # comme avant on met le numéro de la broche dans une variable pour pour pouvoir la rappeler plus tard (à noter que cette fois ci le nom correspond aux "normes" pour les variables, ces normes changent en fonction du language elle pourrait s'appeler "outputPin", l'important est de ne pas mélanger le tout pour garder un ensemble homogène et pouvoir partager son code proprement)
GPIO.setmode(GPIO.BOARD)    # rappel de l'utilité de la commande : on indique que l'on utiliseras des chiffres pour désigner les différents pins
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGHT)    # rappel sur l'utilité de la commande + indication du dernier argument : on désigne le pin corespondant à la valeur de la variable "output_pin" (33) comme étant un pin de sortie (OUT). l'argument "initial=GPIO.HIGHT" indique que par défaut, la valeur de sortie seras HIGHT, donc qu'on y enverras du courant.
pwm = GPIO.PWM(output_pin, 100)     # ici on stoque une fonction dans une variable (oui c'est possible), grâce à ça on pourras appeler "pwm"au lieu de préciser "GPIO.PWM(output_pin, value)" + le 100 correspond à la valeur du courant que l'on injecte dans la led par défaut
pwm.start(0)     # ici on lance la led avec comme "racourcis clique" (valeur en % de l'énergie envoyé par le pin) 0 (donc on envoie aucun courant) 


# -- mise en place du programme principale

try:   # même principe que précedement, on lance le programme jusqu'a ce que l'utilisateur appuie sur les touches ctrl + c dans le terminal
    while 1:        #boucle infinie
        for val in range(100):      # boucle qui fait varier la valeur de la variable val entre "nil"/"null" (valeur par défaut d'une variable non indentée) et 100 
                time.sleep(0.1)
                pwm.ChangeDutyCycle(val)   # ici on utilise la variable val dont la valeur varie entre 0 et 100 pour modifier progressivement l'intensité électrique délivrée

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

         
"""
comme entrainnement pour voir si on a tout compris, il est possible de compléter le programme fournis ci dessus pour faire en sorte qu'une fois la led allumé à 100% elle s'éteigne tout aussi doucement
""" 


### ---< version dans commentaire d'explication du programme >--- ###

import Jetson.GPIO as GPIO
import time

# -- mise en place des variables et du setup nessessaire
output_pin = 33 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGHT)
pwm = GPIO.PWM(output_pin, 100)     
pwm.start(0)


# -- mise en place du programme principale

try:   
    while 1:       
        for val in range(100):      
                time.sleep(0.1)
                pwm.ChangeDutyCycle(val)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
