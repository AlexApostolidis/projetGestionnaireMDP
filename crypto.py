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


readKey()
