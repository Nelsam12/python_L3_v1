from entities.Auteur import Auteur
from entities.Livre import Livre
from repository.Repository import Repository

import json
import os

def dict_to_livre(livre_dict):
    auteur_data = livre_dict['_Livre__auteur']
    auteur = Auteur(
        nom=auteur_data['_Auteur__nom'],
        prenom=auteur_data['_Auteur__prenom'],
        date_naissance=auteur_data['_Auteur__date_naissance'],
        nationalite=auteur_data['_Auteur__nationalite']
    )

    livre = Livre(
        titre=livre_dict['_Livre__titre'],
        auteur=auteur,
        annee_edition=livre_dict['_Livre__annee_edition'],
        genre=livre_dict['_Livre__genre'],
        etat=livre_dict['_Livre__etat'],
        exemplaire=livre_dict['_Livre__exemplaire']
    )
    
    return livre



class LivreRepositoryList(Repository):
    def __init__(self):
        self.__livres = []

    def save(self, livre):
        self.__livres.append(livre)

    def update(self, livre):
        self.__livres[self.__livres.index(livre)]= livre

    def delete(self, id):
        livre = self.select_by_id(id)
        self.__livres.pop(self.__livres.index(livre))

    def select_all(self):
        return self.__livres
    
    def select_by_id(self, id):
        return filter(lambda x: x.id == id, self.__livres)



class LivreRepositoryJson(Repository):
    def __init__(self, filename="./db/json/livres.json"):
        self.filename = filename
        # If the file does not exist, create it with an empty list as initial content
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def _load_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def save(self, entity):
        data = self._load_data()
        livre_dict = entity.set_auteur(entity.get_auteur().__dict__).__dict__
        livre_dict['id'] = len(data) + 1  # Generate a new ID
        data.append(entity.__dict__)
        self._save_data(data)

    def update(self, entity):
        data = self._load_data()
        entity_id = entity.get("id")
        for idx, item in enumerate(data):
            if item['id'] == entity_id:
                data[idx] = entity
                self._save_data(data)
                return
        raise ValueError(f"Entity with id {entity_id} not found.")

    def delete(self, id):
        data = self._load_data()
        new_data = [item for item in data if item['id'] != id]
        if len(new_data) == len(data):
            raise ValueError(f"Entity with id {id} not found.")
        self._save_data(new_data)

    def select_all(self):
        return self._load_data()

    def select_by_id(self, id):
        data = self._load_data()
        for item in data:
            if item['id'] == id:
                return item
        raise ValueError(f"Entity with id {id} not found.")


class LivreRepositoryCsv(Repository):
    def __init__(self):
        pass