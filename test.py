# Permet d'afficher du texte
# Accents et caractères spéciaux uniquement dans chaînes de caractères (" ") et commentaires ( # )
# (Aucun accent ni caractère spécial n'est admis dans les codes)
print("Hello, World!")

print("Bonjour François")

# Variables (espaces de stockage d'information)
nom = "Server01" # Chaine de caractère
age = 18 # Integer (int) ou entier
actif = True # Boolean

# Permet de demander à l'utilisateur quelque chose et de stocker le résultat dans la variable firstName
firstName = input("Entrez votre prénom : ")

print("Bonjour", firstName, "Vous etes sur le", nom)

# La condition sert à comparer deux valeurs
# Si condition:
    # Action si vrai
# Sinon:
    #Action si faux

# def pertmet de créer une fonction
# Cela (la fonction) permet d'avoir du code réutilisable sans le reécrire
# Le parametre "âge" est une variable dont la portée se limite uniquement à l'interieur de la fonction
# Elle n'est donc pas dispo en dehors
# Les espacement sont très importants, pour savoir si l'on est dans la fonction en dehors
def isMajor(age):
    if age >= 18:
        print("Vous êtes majeur, entrez.")
    else:
        print("Vous êtes mineur, sortez, NOW!")

for i in range(5):
    print(i)

# Une liste est un regroupement d'information
# Elle peut contenir du texte, des nombres, des booleans, des objets, d'autres listes, etc
liste = ["François", 42, True, "Vendôme"]

# Pour chaque prénom de la liste
# la varialbe prenom peux être nomée comme on veut, c'est nous qui choisissons son nom
for prenom in liste:
    # J'affiche le prénom
    print(prenom)

isMajor(10)
isMajor(28)
isMajor(18)


