#! /usr/bin/env python3
# import
import random_passWord
import maskpass
from classes import Account
from classes import Password
from classes import User
from classes import Username
from classes import Wallet
from classes import Website

# main
if __name__ == '__main__':

    print("Bienvenue dans votre gestionnaire de mot de passe ! \nConnectez vous au programme :)\n")
    connection_password = maskpass.askpass(mask='*')  # hide password while writing
    connection_to_the_program = Account.verify_account(connection_password)

    while not connection_to_the_program:

        print('Identifiant ou mot de passe incorrecte. Veuillez réssayer.\n')
        username = input("Enter username: ")
        connection_password = maskpass.askpass(mask='*')
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
                    identify = input('Entrez votre identifiant: ')
                    password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')

                    if password == "non":
                        password = input('Entrez votre mot de passe: ')
                    else:
                        password = random_passWord.automatic_random_password()

                    wallet.logs(site, id, password)
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

                case "fin":

                    condition = False
