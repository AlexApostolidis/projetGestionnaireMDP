#immport
import classe
import random_passWord
import logIn



#MAIN
if __name__ == '__main__':

    print("Bienvenue dans votre gestionnaire de mot de passe ! \nConnectez vous au programme :)\n")
    username = input("Nom d'utilisateur: ")
    connexionPassword = input("Mot de passe: ")
    connexionAuProgramme = logIn.connexion(username, connexionPassword) 
    while connexionAuProgramme == False :
        print('Identifiant ou mot de passe incorrecte. Veuillez réssayer.\n')
        username = input("Nom d'utilisateur: ")
        connexionPassword = input("Mot de passe: ")
        connexionAuProgramme = logIn.connexion(username, connexionPassword)

    if connexionAuProgramme == True :
   
        wallet = classe.Wallet()
        data = wallet.ouverture()

        condition = True
        while condition:
            question = input('\nQue voulez vous faire ? \nTaper "nouveau" pour pouvoir ajouter un mot de passe\nTaper "supprimer" pour supprimer un mot de passe\nTaper "modifier" pour modifier un mot de passe \nTaper "afficher" pour afficher un mot de passe \nTaper "enregistrer" pour enregistrer et fermer le programme \nTaper "fin" pour fermer le programme \n=>')
            match question :

                case "nouveau":
                    site = input('Entrez un nouveau site: ')
                    id = input('Entrez votre identifiant: ')
                    passWord = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                    if passWord == "non":
                        passWord = input('Entrez votre mot de passe: ')
                    else : passWord = random_passWord.mot_de_passe()
                    wallet.logs(site, id, passWord)
                    print('\n---------- Le mot de passe du site "' + site + '" a bien été ajouté ----------\n')
                    print("- "+ site + " | identifiant: " + id + " | password: " + passWord + "\n")


                case "supprimer":
                    supprimer = input('Quelle mot de passe voulez vous supprimer ? Entrez le site en question ')
                    print('\n---------- Le mot de passe du site "' + site + '" a bien été supprimé ----------\n')
                    wallet.supprimer(supprimer)


                case "modifier":
                    site = input('Quel mot de passe voulez vous modifier ? Entrez le site en question ')
                    mdp = wallet.modifier(site)
                    print('\n---------- Le mot de passe du site "' + site + '" a bien été modifié ----------\n')
                    wallet.nouveau(site, mdp)


                case "enregistrer":
                    wallet.enregistrer()
                    print('---------- Vos mots de passe ont bien été enregistrés ----------')

                case "afficher":
                    wallet.affichage()

                case "fin":
                    condition = False

        

    
