import random


def automatic_random_password():

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "!«#$%&()*+-./:;><=?@[]^}{~"
    use_for = lower_case + upper_case + number + symbol
    length_to_pass = 15
    password = "".join(random.sample(use_for, length_to_pass))

    return password
