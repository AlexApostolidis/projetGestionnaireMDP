from ast import main



class Wallet:
    """pour stocker les mots de passe en ajouter et les modifier"""

    def __init__(self):
        self._passWords = []

   
    def passWords(self, new_site, new_identify, new_passWord):
        self._passWords.append({'site':new_site, 'id' : new_identify, 'passWord':new_passWord})

    def __str__(self):
        return str(self._passWords)






 


