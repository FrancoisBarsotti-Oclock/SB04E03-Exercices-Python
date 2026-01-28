# Exercice 02 - Condition
# Demander l'âge et afficher Majeur ou Mineur

age = input("Quelle est votre âge ? ")

# J'essaie de transformer mon âge en nombre
try:
    # Si oui, on tranforme âge (qui de base est une chaine de caractères, ou string) en INT (Nombre entier)
    age = int(age)
except:
    # Si jamais il y a une erreur, au lieu de crash mon script
    # J'arrive dans l'except, et j'affice un message d'erreur moi même avant d'exit le script
    print("Merci d'entrer un nombre valide")
    exit()

if age >= 18:
    print("Majeur")
    exit()
# On peut rajouter else if (elif pour python) comme troisième condition
elif age < 0:
    print("Vous n'êtes pas encore né")
else:
    print("Mineur")