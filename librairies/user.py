import json


class User:
    """
    """

    def __init__(self):
        with open("connexionId.json", "r") as user_data:
            data = json.load(user_data)
        self._first_name = data["firstname"]
        self._last_name = data["lastname"]
        self._security_question = data["question"]

    @staticmethod
    def write_names(firstname, lastname, question):
        with open("connexionId.json", "r") as user_data:
            data = json.load(user_data)
        data["firstname"] = firstname
        data["lastname"] = lastname
        data["question"] = question
        with open("connexionId.json", "w") as user_data:
            json.dump(data, user_data)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def question(self):
        return self._security_question

    def __str__(self):
        return f"Bonjour monsieur{self._last_name} {self._first_name}."
