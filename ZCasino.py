import os
from random import randrange
from math import ceil
import time

# Variables
my_money = 1000  # Le joueur a 1000$ au debut de la partie
continue_the_game = True  # la partie continue tant quelle est vrai

print("Vous vous installez a la table de la roulette. Vous avez :", my_money, "$")

while continue_the_game:
    my_number = -1

    while my_number < 0 or my_number > 49:
        print("Vous avez avec vous :", my_money, "$")
        time.sleep(2)
        my_number = int(input("Entrez votre nombre entre 0 et 49 : "))

        if 49 < my_number or my_number < 0:
            print("Error Wrong number please retry !")
            continue
    my_price = 0
    while my_price <= 0 or my_price > my_money:
        my_price = int(input("Entrez votre mise : "))

        if my_money < my_price:
            print("Error: You don't have enough money, please retry.")
        elif my_price <= 0:
            print("Error: Negative price or null, please retry.")
            continue
    print("Vous avez choisi le nombre :", my_number, "Vous avez misez :", my_price, "$")
    time.sleep(2)
    my_money -= my_price
    print("Il vous reste alors :", my_money, "$")
    time.sleep(2)

    print("Lancement de la bille.....")
    time.sleep(4)

    winner_number = randrange(50)
    print("La roulette tourne......... Attention.... Et la bille s'arrête sur le numero :", winner_number)
    time.sleep(2)
    # Le joueur gagne :
    # Meme nombre = 3* my price
    if my_number == winner_number:
        reward = 3 * my_price + my_price
        print("Vous avez ganez : 3 *", my_price, "+", my_price, "=", reward, "$ car vous avez exatement le meme nombre")
        time.sleep(2)
        print("Vous avez un total de :", my_money, "+", reward)
        time.sleep(2)
        my_money += reward
        print("Votre compte est de :", my_money, "$")
        time.sleep(2)
        
    # Nombre paire ou impaire = 50% de my price + my price
    elif winner_number % 2 == 0 and my_number % 2 == 0 and my_number != winner_number:
        reward = my_price + (my_price * 0.5)
        print("Vous avez ganez 50% de votre mise : 0.5 *", my_price, "+", my_price, "=", ceil(reward),
              "$ car votre nombre est paire comme le nombre gagnant")
        time.sleep(2)
        print("Vous avez un total de :", my_money, "+", ceil(reward))
        time.sleep(2)
        my_money += ceil(reward)
        print("Votre compte est de :", my_money, "$")
        time.sleep(2)
        
    elif winner_number % 2 != 0 and my_number % 2 != 0 and my_number != winner_number:
        reward = my_price + (my_price * 0.5)
        print("Vous avez ganez 50% de votre mise : 0.5 *", my_price, "+", my_price, "=", ceil(reward),
              "$ car votre nombre est impaire comme le nombre gagnant")
        time.sleep(2)
        
        print("Vous avez un total de :", my_money, "+", ceil(reward))
        time.sleep(2)
        
        my_money += ceil(reward)
        print("Votre compte est de :", my_money, "$")
        time.sleep(2)
        
    # Rien = perdu my price
    else:
        print("Vous avez perdu")
        time.sleep(2)
        print("Votre argent est de :", my_money, "$")
        
    if(my_money <= 0) :
        print("Vous n'avez plus d'argent ! \nDommage, au revoir !")
        continue_the_game = False


