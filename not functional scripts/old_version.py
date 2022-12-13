# Wallet :
# def display_wallet(self):
#    """
#        display the overview of the list
#        param: none
#        return: none
#    """
#    for i in self._wallet:
#        print("\n- " + i['site'] + " | identifiant: " + i['id'] + " | mot de passe: " + i['password'] + " \n")

# def save_wallet(self):
#    """
#        save list in a JSON file
#        param: none
#        return: none
#    """
#    with open('data.json', 'w') as file:
#        json.dump(self._wallet, file)

# def opening_json(self):
#    """
#        allow to open a JSON file and add the list in
#        param:  none
#        return: updated list
#    """
#    with open('data.json') as read:
#        reading = json.load(read)
#    for i in reading:
#        self._wallet.append(i)
#    return self._wallet

# @staticmethod
# def create_password():
#    """
#       create a new password (automatic or not)
#       param: none
#       return: string the new password
#    """
#    ask_auto_password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ').lower()
#    if ask_auto_password == "non":
#        next_password = input('entrez le nouveau mot de passe: ')
#        return next_password
#    next_password = random_passWord.automatic_random_password()
#    return next_password

# Account:
# @staticmethod
# def create_account(password):
#    if password == "":
#        raise (ValueError, "password is empty")
#    with open("data/connexionId.json", 'r') as file:
#        json_dictionnary = json.load(file)

#    json_dictionnary["user"]["password"] = password
#    with open("data/connexionId.json", 'w') as writing_pass:
#        json.dump(json_dictionnary, writing_pass)

# @staticmethod
# def renew_password():
#    """
#       create a new password (automatic or not)
#       param: none
#       return: string the new password
#    """
#    next_password = input('entrez le nouveau mot de passe: ')
#    return next_password

# @staticmethod
# def new_password():
#    new_password = input(" : ")
#    return new_password

# @staticmethod
# def edit_application_password(new_password):
#    """
#        write the new_password for the application
#        param:
#            new_password: the new password
#        return: none
#    """
#    with open("connexionId.json", 'r') as file:
#        json_dictionnary = json.load(file)

#    json_dictionnary["user"]["password"] = new_password
#    with open("connexionId.json", 'w') as writing_pass:
#        json.dump(json_dictionnary, writing_pass)

