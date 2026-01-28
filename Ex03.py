# Exercice 03: Boucle et liste
# Créer une liste de machines et les afficher.

# On choisi soi-même le nom de la variable (en bleu ci-dessous)
ListeDeMachines = ["Café", "Machine01", "Machine02", "Machine03"]

OS = ["Win10", "Win11", "Linux", "MacOs"]

# On peut séparer les listes, avec un titre, si l'on veut
print("======= Première boucle =======")
#Début de la première boucle
# On va recupérer chaque machine à l'unité dans notre liste (chaque élément un par un)
for machine in ListeDeMachines:
    print(machine)
# Fin de la première boucle

# On peut aussi faire un retour à la ligne pour mieux séparer les listes
print("")

#Début de la deuxième boucle
print("======= Deuxième boucle =======")
for system in OS:
    print(system)
# Fin de la deuxième boucle