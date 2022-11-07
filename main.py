#immport
import classe
import json
import random_passWord


#MAIN
if __name__ == '__main__':

   
    wallet = classe.Wallet()
    with open ('data.json') as read:
        lectur = json.load(read)
    
    for i in lectur:
        wallet._passWords.append(i)


    print("Bienvenue dans votre gestionnaire de mot de passe ! \n")
    condition = True
    while condition:
        question = input('Que voulez vous faire ? \nTaper "nouveau" pour pouvoir ajouter un mot de passe\nTaper "supprimer" pour supprimer un mot de passe\nTaper "modifier" pour modifier un mot de passe \nTaper "afficher" pour afficher un mot de passe \nTaper "enregistrer" pour enregistrer et fermer le programme \n=>')
        match question :

            case "nouveau":
                site = input('Entrez un nouveau site: ')
                id = input('Entrez votre identifiant: ')
                passWord = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                if passWord == "non":
                    passWord = input('Entrez votre mot de passe: ')
                else : passWord = random_passWord.mot_de_passe()
                wallet.logs(site, id, passWord)
                wallet.affichage()

            case "supprimer":
                supprimer = input('Quelle mot de passe voulez vous supprimer ? Entrez le site en question ')
                wallet.supprimer(supprimer)
                wallet.affichage()

            case "modifier":
                modifier = input('Quel mot de passe voulez vous modifier ? Entrez le site en question ')
                for i in wallet._passWords:
                    if i['site'] == modifier:
                        nouveau_mot_de_passe = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                        if nouveau_mot_de_passe == "non":
                            nouveau_mot_de_passe = input('entrez le nouveau mot de passe: ')
                        else : nouveau_mot_de_passe = random_passWord.mot_de_passe()
                        wallet.nouveau(modifier, nouveau_mot_de_passe)
                        wallet.affichage()

            case "enregistrer":
                condition = False

            case "afficher":
                wallet.affichage()



    with open('data.json', 'w') as file:
        json.dump(wallet._passWords, file)
        

    
