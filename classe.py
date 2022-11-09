from ast import main



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
                
        

    def affichage(self):
        for i in self._passWords:
            print("\n- " + i['site'] + " | identifiant: " + i['id'] + " | mot de passe: " + i['passWord'] + " \n")






 


