import json
import librairies


class Wallet:
    """Class representing a Wallet where a user can store his Usernames and Passwords from Websites

    Authors: Shayann Gonzalez, Apostolidis Alex, Thomas Jacob
    Date : 13/12/2022
    """

    def __init__(self, data):
        """It instantiates a list with dictionaries
        PRE :
             :param data: has to be a list and can be empty.

        POST : create a wallet property who is a list with dictionaries in
        """
        if type(data) != list:
            raise ValueError("Data is not a list")
        self._wallet = []
        for i in data:
            self._wallet.append(i)

    def __len__(self):
        """The size of wallet
        PRE : -
        POST :
              :return: len of wallet
        """
        return len(self._wallet)

    @property
    def wallet(self):
        """The wallet

        PRE : -
        POST :
              :return: return the wallet property
        """
        return self._wallet

    def add_new_logs(self, new_site, new_identify, new_password):
        """Adding a dictionary with one website, one username and one password

        PRE:
            :param new_site: is instance of the class Website, it's a website
            :param new_identify: is instance of Username class, it's the username of the website
            :param new_password: is instance of Password class,  it's the password of the username
        POST: It adds a new dictionary to wallet with an index, a website, a username and a password
        """
        if isinstance(new_site, librairies.Website):
            raise ValueError("Site is not a Website object")
        if isinstance(new_password, librairies.Password):
            raise ValueError("Password is not a Password object")
        if isinstance(new_identify, librairies.Username):
            raise ValueError("Identify is not a Username object")
        self._wallet.append({'index': len(self._wallet) + 1, 'site': new_site.name, 'id': new_identify.username,
                             'password': new_password.password})

    def edit_site_password(self, site, new_password):
        """Edit a password from the wallet

        PRE :
             :param site: it's an integer, and it's the index of the password you need to edit
             :param new_password:  can't be None or empty
        POST : The password from the wallet changed with the new password
        """
        try:
            int(site)
            if new_password is None or new_password == "":
                raise ValueError("Password is empty")
            for i in self._wallet:
                if i['index'] == int(site):
                    i['password'] = new_password
        except Exception:
            raise ValueError("Index not a integer")

    def delete_site_password(self, site):
        """Delete a dictionary from the wallet

        PRE :
             :param site: is an integer, and it's the index of the dictionary you want to delete
        POST : The dictionary with the index is deleted
        """
        try:
            int(site)
            self._wallet.pop(site)
            for j in range(len(self._wallet)):
                self._wallet[j]['index'] = j + 1
        except Exception:
            raise ValueError("Index not a integer")


# Saving the wallet in json method
def save_wallet(data_saving):
    """It's saving a list in a json file

    PRE :
            :param data_saving: it's a list
    POST : It writes the list in a json file
    """
    if type(data_saving) != list:
        raise ValueError("Data is not a list")
    with open('data/data.json', 'w') as file:
        json.dump(data_saving, file)
