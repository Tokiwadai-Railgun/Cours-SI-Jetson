(skip d'une partie de vidéo, à compléter plus tard)

commandes dans l'ordre : 

## installations des dépendances nessessaires :
sudo chmod +x install.sh  ## --> ça permet de d'annoncer le fichier install.sh en tant que fichier executable

./install.sh ## --> execution du fichier install.sh 

En cas de prolbème lors de l'installation faire --> git config --global proxy.http://172.16.0.1:3128


**relancer terminal**

nvm install node | nvm use node ## --> installation et utilisation de node 

sudo apt install python3-pip | sudo apt install python-pip ## --> installation de pip sur les différentes versions de python

-- pip c'est quoi?
--> pour comprendre il faut déjà savoir sur quoi on execute nos commandes dans le terminal, elles sont executés en bash le language machine. pip c'est la même chose sauf que c'est réservé au language python et non à la machine. Avec la commande "pip" ("pip install" par exemple) on précise que l'on veut non pas utiliser le bash mais pip et donc on installe des dépendances python au lieu de packages linux.


## installation de jupiter notebook 
pip3 install pyzmq==17.0.0  ## --> déjà oui il y a deux =, ensuite le 17.0.0 correspond à une version compatible avec Jetson Nano de pyzmq, si on ne le précise pas iul va en télécharger une non compatible

pip3 install --upgrade pip | pip3 install --upgrade pip3  ## --> mise à jours de pip sur python et python 3, nessessaire pour la suite

sudo pip install jupyter ## --> installation de jupyter notebook (oui enfin)

-- il y auras peut-être une erreur indiquant qu'un paquet n'a pas été installé, dans ce cas il faudrat le faire manuellement via la commande ci dessous (executer la commande alors que le paquage est déjà installé ne provoque aucune erreure)

sudo apt install libffi ## --> remplacer "libffi" par le nom du paquet indiqué par l'erreur si celui-ci est différent
