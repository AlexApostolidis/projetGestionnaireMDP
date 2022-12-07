import random


def automatic_random_password():
    """
    generate a random password based on the following data
    param: none
    return: a string of random elements
    """

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "01234567890123456789"
    symbol = "!«#$%&()*+-./:;><=?@[]^}{~"
    use_for = lower_case + upper_case + number + symbol
    length_to_pass = 15
    password = "".join(random.sample(use_for, length_to_pass))

    return password

