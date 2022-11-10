from cryptography.fernet import Fernet

def create_key():

    hashing_key = Fernet.generate_key()
    hashing_key = Fernet(hashing_key)

    return hashing_key

def crypt_message(message, hashing_key):

    crypted_message = hashing_key.encrypt(message.encode())

    return crypted_message

def decrypt_message(message, hashing_key):

    decrypt_message = hashing_key.decrypt(message).decode()

    return decrypt_message

h = create_key()
m = 'test'
m = crypt_message(m, h)
print(m)
m = decrypt_message(m, h)
print(m)