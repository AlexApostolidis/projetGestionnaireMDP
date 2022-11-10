from ast import main
import random_passWord
import json


class Wallet:
    """pour stocker les mots de passe en ajouter et les modifier"""

    def __init__(self):
        self._passwords = []

   
    def logs(self, new_site, new_identify, new_password):
        self._passwords.append({'site':new_site, 'id' : new_identify, 'password':new_password})

    def __str__(self):
        return str(self._passwords)

    def create_password(self,site, new_password):
         for i in self._passwords:
            if i['site'] == site:
                i['password'] = new_password
                

    def delete_password(self, site):
        for i in self._passwords:
            if i['site'] == site:
                self._passwords.remove(i)


    def edit(self, new_password):
        for i in self._passwords:
            if i['site'] == new_password:
                next_password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')
                if next_password == "non":
                    next_password = input('entrez le nouveau mot de passe: ')
                else : next_password = random_passWord.automatic_random_password()
                
        return next_password
                
        

    def viewing(self):
        for i in self._passwords:
            print("\n- " + i['site'] + " | identifiant: " + i['id'] + " | mot de passe: " + i['password'] + " \n")



    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self._passwords, file)


    def opening(self):
        with open ('data.json') as read:
            reading = json.load(read)
        for i in reading:
            self._passwords.append(i)
        return self._passwords