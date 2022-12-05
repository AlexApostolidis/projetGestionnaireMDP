#! /usr/bin/env python3
# import
import json
import random_passWord
# import maskpass
from classes import Account
from classes import Password
from classes import User
from classes import Username
from classes import Wallet
from classes import Website

# main
if __name__ == '__main__':

    with open('connexionId.json', 'r') as user_data:
        data_json = json.load(user_data)

    if data_json["firstname"] == "" or data_json["lastname"] == "":
        print('Bonjour veuillez indiquer votre nom et prénom')
        firstname = input("Quelle est votre prénom : ")
        lastname = input("Quelle est votre nom : ")
        while firstname == "" or lastname == "":
            firstname = input("Quelle est votre prénom : ")
            lastname = input("Quelle est votre nom : ")
        user_app = User.write_names(firstname, lastname)

    if data_json["user"]["password"] == "":
        print("Veuillez vous créer un mot de passe")
        new_password = input(" => ")
        while new_password == "":
            print("Veuillez vous créer un mot de passe")
            new_password = input(" => ")
        Account.create_account(new_password)

    print("Bienvenue dans votre gestionnaire de mot de passe ! \nConnectez vous au programme :)\n")
    connection_password = input("MDP : ")  # hide password while writing
    connection_to_the_program = Account.verify_account(connection_password)

    while not connection_to_the_program:

        print('Mot de passe incorrecte. Veuillez réssayer.\n')
        connection_password = input("MDP : ")
        connection_to_the_program = Account.verify_account(connection_password)

    if connection_to_the_program:

        wallet = Wallet()
        data = wallet.opening()
        condition = True

        while condition:

            question = input('\nQue voulez vous faire ?\n'
                             'Taper "nouveau" pour pouvoir ajouter un mot de passe\n'
                             'Taper "supprimer" pour supprimer un mot de passe\n'
                             'Taper "modifier" pour modifier un mot de passe \n'
                             'Taper "afficher" pour afficher un mot de passe \n'
                             'Taper "enregistrer" pour enregistrer et fermer le programme\n'
                             'Taper "fin" pour fermer le programme \n=>')

            match question:

                case "nouveau":

                    site = input('Entrez un nouveau site: ')
                    website_obj = Website(site)
                    identify = input('Entrez votre identifiant: ')
                    username_obj = Username(identify)
                    password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                    if password == "non":
                        password = input('Entrez votre mot de passe: ')
                        password_obj = Password(password)
                    else:
                        password = random_passWord.automatic_random_password()
                        password_obj = Password(password)

                    wallet.logs(website_obj, username_obj, password_obj)
                    print(f'\n---------- Le mot de passe du site "{site}" a bien été ajouté ----------\n')
                    print(f"- {site} | identifiant: {identify} | password: {password}\n")

                case "supprimer":

                    delete = input('Quelle mot de passe voulez vous supprimer ? Entrez le site en question ')
                    print(f'\n---------- Le mot de passe du site "{delete}" a bien été supprimé ----------\n')
                    wallet.delete_password(delete)

                case "modifier":

                    site = input('Quel mot de passe voulez vous modifier ? Entrez le site en question ')
                    password = wallet.create_password()
                    print(f'\n---------- Le mot de passe du site "{site}" a bien été modifié ----------\n')
                    wallet.edit_site(site, password)

                case "enregistrer":

                    wallet.save()
                    print('\n---------- Vos mots de passe ont bien été enregistrés ----------')

                case "afficher":

                    wallet.viewing()

                case "BITE":

                    pass

                case "fin":

                    condition = False
