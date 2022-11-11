import random_passWord
import json


class Wallet:
    """
    A wallet for all the passwords and identificators
    param: none
    return: none
    @authors: Apostolidis Alex, Gonzalez Shayann, Jacob Thomas
    """

    def __init__(self):
        """
            initiate a list to stock identificators
            param: none
            return: none
        """

        self._passwords = []

    def logs(self, new_site, new_identify, new_password):
        """
            fill a list with the parameters
            param:
                new_site: name of the sew website you want to add
                new_identify: the username on the website
                new_password: the password for this website
            return: none
        """

        self._passwords.append({'site': new_site, 'id': new_identify, 'password': new_password})

    @property
    # getter method
    def __str__(self):

        return str(self._passwords)

    def edit_site(self, site, new_password):
        """
            write the new_password on the site
            param:
                site: the website which the function is changing the password
                new_password: the new password
            return: none
        """
        for i in self._passwords:
            if i['site'] == site:
                i['password'] = new_password

    def delete_password(self, site):
        """
            remove a website from the list
            param:
                site: the website to remove from the list
            return: none
        """
        for i in self._passwords:
            if i['site'] == site:
                self._passwords.remove(i)

    @staticmethod
    def create_password():
        """
           create a new password (automatic or not)
           param: none
           return: string the new password
        """
        ask_auto_password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ').lower()
        if ask_auto_password == "non":
            next_password = input('entrez le nouveau mot de passe: ')
            return next_password
        next_password = random_passWord.automatic_random_password()
        return next_password

    def viewing(self):
        """
            display the overview of the list
            param: none
            return: none
        """

        for i in self._passwords:
            print("\n- " + i['site'] + " | identifiant: " + i['id'] + " | mot de passe: " + i['password'] + " \n")

    def save(self):
        """
            save list in a JSON file
            param: none
            return: none
        """

        with open('data.json', 'w') as file:
            json.dump(self._passwords, file)

    def opening(self):
        """
            allow to open a JSON file and add the list in
            param:  none
            return: updated list
        """

        with open('data.json') as read:
            reading = json.load(read)
        for i in reading:
            self._passwords.append(i)
        return self._passwords
