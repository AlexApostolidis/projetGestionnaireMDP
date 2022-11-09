from ast import main
import random_passWord
import json


class Wallet:
    """pour stocker les mots de passe en ajouter et les modifier"""

    def __init__(self):
        self._passWords = []

   
    def logs(self, new_site, new_identify, new_passWord):
        self._passWords.append({'site':new_site, 'id' : new_identify, 'passWord':new_passWord})

    def __str__(self):
        return str(self._passWords)

    def nouveau(self,site, new_passWord):
         for i in self._passWords:
            if i['site'] == site:
                i['passWord'] = new_passWord
                

    def supprimer(self, site):
        for i in self._passWords:
            if i['site'] == site:
                self._passWords.remove(i)


    def modifier(self, new_passWord):
        for i in self._passWords:
            if i['site'] == new_passWord:
                nouveau_mot_de_passe = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                if nouveau_mot_de_passe == "non":
                    nouveau_mot_de_passe = input('entrez le nouveau mot de passe: ')
                else : nouveau_mot_de_passe = random_passWord.mot_de_passe()
                
        return nouveau_mot_de_passe
                
        

    def affichage(self):
        for i in self._passWords:
            print("\n- " + i['site'] + " | identifiant: " + i['id'] + " | mot de passe: " + i['passWord'] + " \n")



    def enregistrer(self):
        with open('data.json', 'w') as file:
            json.dump(self._passWords, file)


    def ouverture(self):
        with open ('data.json') as read:
            lectur = json.load(read)
        for i in lectur:
            self._passWords.append(i)
        return self._passWords



 


