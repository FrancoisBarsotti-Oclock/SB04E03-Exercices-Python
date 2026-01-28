# Exercise Final
# On dispose d’une liste de prénoms autorisés à entrer dans une salle.
# On demande à l'utilisateur d'entrer son prénom.
# On parcourt la liste des prénoms
# Conditions: Si le prénom est présent (Accès autorisé) Vs. non présent (Accès interdit)
# Faire que les bons prénoms soient acceptés en majuscules et en minuscules

nameList = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Strip permet de supprimer les espaces inutiles avant et après une chaîne de caractères (réponse)
askedName = input("Votre prénom, svp : ").strip()

# len () permet de compter le nombre d'élements d'une liste
print("Il y a", len(nameList), 'personnes autorisées')

for name in nameList :
    # lower() permet de transformer une chaîne de caractères en minuscule
    if name.lower() == askedName.lower():
        # le f est utilisé pour mettre des variables dans une chaîne de caractères
        print(f"Bonjour {name}, come in!")
        exit()

        print("Vous n'y êtes pas inclus, bye!")
