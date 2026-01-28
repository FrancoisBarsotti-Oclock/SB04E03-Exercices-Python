# Challenge B403 - Jeu sur Python: "C'est plus !  C'est moins !"
    # Le programme choisit un nombre sécret aléatoire et l'utilisateur doit le deviner, avec les conditions suivantes:
        # Tant que le nombre n'est pas trouvé:
            # Si le nombre proposé est trop petit, afficher: C'est plus !
            # s’il est trop grand, afficher : C'est moins !
    # Quand l’utilisateur trouve le bon nombre, afficher : Bravo, vous avez trouvé !
    # À chaque proposition, le compteur de tentatives augmente: son nombre total doit s'afficher à la fin du jeu.
    # À la fin du jeu, demander à l'utilisateur s'il souhaite rejouer, pour redémarrer (oui) ou arrêter le programme (non).

import random

def plus_ou_moins():
    print("Venez jouer au 'C'est plus ! C'est moins !'")

    # 1. On paramètre le choix aléatoire du nombre secret (1-15)
    ramdom_number = random.randint(1, 15)
    attemps = 0

    # 2. Boucle du nombre de tentatives
    while True:
        try:
            proposition = int(input("Entre 1 et 15, à quel nombre est-ce que je pense ?) : "))
        except ValueError:
            print("Essayez plutôt un nombre entier.")
            continue

        attemps += 1 # Comptage du nombre d'essais ou tentatives

        if proposition < ramdom_number:
            print("C'est plus !")
        elif proposition > ramdom_number:
            print("C'est moins !")
        else:
            print(f"Bravo, vous avez trouvé ! Et ça en un total de {attemps} tentatives !")            
            break

def main():
    while True: # Boucle de redémarrage, au choix du joueur
        plus_ou_moins()
        play_again = input("Souhaitez-vous rejouer ? (oui/non) : ").strip().lower()
        if play_again != "oui":
            print("À bientôt !")
            break

if __name__ == "__main__":
    main()


