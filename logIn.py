import json

def connexion(userName, connexionPassword):
    with open("connexionId.json") as file : 
        doc = json.load(file)
    return doc['logUtilisateur']['userName'] == userName and doc['logUtilisateur']['passWord'] == connexionPassword