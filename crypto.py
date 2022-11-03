import rsa

def createKey():

    public_key, private_key = rsa.newkeys(1024)

    with open('C:/Users/alexa/OneDrive/Bureau/data_public.pem', 'wb') as file:
        file.write(public_key.save_pkcs1('PEM'))

    with open('C:/Users/alexa/OneDrive/Bureau/data_private.pem', 'wb') as file:
        file.write(private_key.save_pkcs1('PEM'))

def readKey():

    with open('C:/Users/alexa/OneDrive/Bureau/data_public.pem', 'rb') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())

    with open('C:/Users/alexa/OneDrive/Bureau/data_private.pem', 'rb') as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())

    return public_key, private_key

def cryptMessage(message):

    keys = readKey()
    public_key = keys[0]
    crypt_message = rsa.encrypt(message.encode(), public_key)
    return crypt_message

def decryptMessage(message):

    keys = readKey()
    private_key = keys[1]
    decrypt_message = rsa.decrypt(message, private_key)
    return decrypt_message
