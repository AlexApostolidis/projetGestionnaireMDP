#immport

import tkinter
from tkinter import *
import classe
import json
import random_passWord


if __name__ == '__main__':

   
    wallet = classe.Wallet()
    with open ('data.json') as read:
        lectur = json.load(read)
    
    for i in lectur:
        wallet._passWords.append(i)



    condition = True
    while condition:
        question = input('entrez votre demande: ')
        match question :

            case "nouveau":
                site = input('entrez le site: ')
                id = input('entrez votre identifiant: ')
                passWord = input('voulez vous un mot de passe généré automatiquement ? ')
                if passWord == "non":
                    passWord = input('entrez votre mot de passe: ')
                else : passWord = random_passWord.mot_de_passe()
                wallet.logs(site, id, passWord)
                print(wallet)

            case "supprimer":
                supprimer = input('quelle mot de passe voulez vous supprimer ? ')
                wallet.supprimer(supprimer)
                print(wallet)
                break

            case "modifier":
                modifier = input('quel mot de passe voulez vous modifier ? ')
                for i in wallet._passWords:
                    if i['site'] == modifier:
                        nouveau_mot_de_passe = input('entrez le nouveau mot de passe: ')
                        wallet.nouveau(modifier, nouveau_mot_de_passe)
                        print(wallet)

            case "stop":
                condition = False



    with open('data.json', 'w') as file:
        json.dump(wallet._passWords, file)
        

    
# #screen
#     screen = tkinter.Tk()
#     screen.geometry('1280x720')
#     screen.title("Gestionnaire de mot de passe")




#     #affichage écran
#     essai = Label(text="test", )
#     essai.pack()
#     screen.mainloop()   #empêche de fermer la fenêtre