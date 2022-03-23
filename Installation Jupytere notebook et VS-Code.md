(skip d'une partie de vidéo, à compléter plus tard)

commandes dans l'ordre : 

## installations des dépendances nessessaires :
sudo chmod +x install.sh  ## --> ça permet de d'annoncer le fichier install.sh en tant que fichier executable

./install.sh ## --> execution du fichier install.sh 

**relancer terminal**

nvm install node | nvm use node ## --> installation et utilisation de node 

sudo apt install python3-pip | sudo apt install python-pip ## --> installation de pip sur les différentes versions de python


## installation de jupiter notebook 
pip3 install pyzmq==17.0.0  --> déjà oui il y a deux =, ensuite le 17.0.0 correspond à une version compatible avec Jetson Nano de pyzmq, si on ne le précise pas iul va en télécharger une non compatible
pip3 install --upgrade pip | pip3 install --upgrade pip3  --> mise à jours de pip sur python et python 3, nessessaire pour la suite

sudo pip install jupyter --> installation de jupyter notebook (oui enfin)
-- il y auras peut-être une erreur qui diras que un paquet n'a pas été installé, dans ce cas executer la commande en dessous (de toute façon le faire même si il est installé ne change rien)
sudo apt install libffi
