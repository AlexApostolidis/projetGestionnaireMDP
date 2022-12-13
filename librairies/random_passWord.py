import random


def automatic_random_password():
    """It generates a random password based on datas picked randomly

    PRE: none
    POST: return a string of 15 characters made of lower cases, upper cases, numbers and non-alphanumeric characters
          picked randomly
    """

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "01234567890123456789"
    symbol = "!«#$%&()*+-./:;><=?@[]^}{~"
    use_for = lower_case + upper_case + number + symbol
    length_to_pass = 15
    password = "".join(random.sample(use_for, length_to_pass))

    return password

