import random 



def mot_de_passe():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "@#$€%/?&+-*"

    Use_for = lower_case + upper_case + number + symbol
    length_to_pass = 12

    passWord = "".join(random.sample(Use_for, length_to_pass))
    return passWord

