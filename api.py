from flask import *
import json, os

pathFile = os.environ['HOME']

app = Flask(__name__)

#_______________  Fonctions ____________
def readData():
    result=""
    fichier = open("c:/Users/Utilisateur/Documents/aws/tstApach/jefe.json", "r")
    for ligne in fichier:
        result+=ligne
    fichier.close()
    return result
    

def putData(data):
    result = False
    fichier = readData()
    dataJSON = json.loads(fichier)
    dataJSON["test2"].append(data)
    print("test :",json.dumps(dataJSON))

    with open("c:/Users/Utilisateur/Documents/aws/tstApach/jefe.json", "w") as outfile:
        json.dump(dataJSON, outfile)
    result=True
    return result


#_______________  ROUTES _______________

@app.route('/v1/hello-world')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['GET'])
def parse_request_get():
    # Votre fonction pour lire les data d'un fichier

    data = readData()
    return data

@app.route('/data', methods=['POST'])
def parse_request_post():
    data = request.data  # Le payload de votre requete
    result = putData(data)
    return result


if __name__ == '__main__':
    app.run("0.0.0.0")