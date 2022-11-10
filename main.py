#! /usr/bin/env python3
#immport
import classe
import random_passWord
import logIn
import maskpass


#MAIN
if __name__ == '__main__':


    print("Bienvenue dans votre gestionnaire de mot de passe ! \nConnectez vous au programme :)\n")
    username = input("Enter username: ")
    connection_password = maskpass.askpass(mask='*')
    connection_to_the_program = logIn.connection(username, connection_password) 
    while connection_to_the_program == False :
        print('Identifiant ou mot de passe incorrecte. Veuillez réssayer.\n')
        username = input("Enter username: ")
        connection_password = maskpass.askpass(mask='*')
        connection_to_the_program = logIn.connection(username, connection_password)

    if connection_to_the_program == True :
   
        wallet = classe.Wallet()
        data = wallet.opening()

        condition = True
        while condition:
            question = input('\nQue voulez vous faire ? \nTaper "nouveau" pour pouvoir ajouter un mot de passe\nTaper "supprimer" pour supprimer un mot de passe\nTaper "modifier" pour modifier un mot de passe \nTaper "afficher" pour afficher un mot de passe \nTaper "enregistrer" pour enregistrer et fermer le programme \nTaper "fin" pour fermer le programme \n=>')
            match question :

                case "nouveau":
                    site = input('Entrez un nouveau site: ')
                    id = input('Entrez votre identifiant: ')
                    password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                    if password == "non":
                        password = input('Entrez votre mot de passe: ')
                    else : password = random_passWord.automatic_random_password()
                    wallet.logs(site, id, password)
                    print('\n---------- Le mot de passe du site "' + site + '" a bien été ajouté ----------\n')
                    print("- "+ site + " | identifiant: " + id + " | password: " + password + "\n")


                case "supprimer":
                    delete = input('Quelle mot de passe voulez vous supprimer ? Entrez le site en question ')
                    print('\n---------- Le mot de passe du site "' + site + '" a bien été supprimé ----------\n')
                    wallet.delete_password(delete)


                case "modifier":
                    site = input('Quel mot de passe voulez vous modifier ? Entrez le site en question ')
                    password = wallet.edit(site)
                    print('\n---------- Le mot de passe du site "' + site + '" a bien été modifié ----------\n')
                    wallet.create_password(site, password)


                case "enregistrer":
                    wallet.save()
                    print('\n---------- Vos mots de passe ont bien été enregistrés ----------')

                case "afficher":
                    wallet.viewing()

                case "fin":
                    condition = False