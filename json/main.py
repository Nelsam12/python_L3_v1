import json as js
import os
def get_data(filename) -> list[dict]:
    data = []
    if os.path.exists(PATH):
        with open(filename, "r") as f:
            data = js.load(f)
    return data

def insert_data(filename, data):
    donnees = get_data(PATH) # Recupération des données depuis le JSON
    donnees.append(data) # Ajout de la donnée aux données du JSON
    with open(filename, "w") as f:
        js.dump(donnees, f, indent = 4)

PATH = "test.json"

donnees = get_data(PATH)
person = {
    "nom": "Doe",
    "prenom": "John",
    "age": 30
}

print("Données initiales:")
print("AVANT INSERTION")
print(get_data(PATH))
print("APRES INSERTION")
insert_data(PATH, person)
print(get_data(PATH))

