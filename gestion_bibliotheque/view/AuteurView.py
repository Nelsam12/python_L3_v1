
from entities.Livre import Livre
from entities.Auteur import Auteur


class AuteurView:
    def __init__(self):
        pass

    def create(self) -> "Auteur":
        nom = input("Entrez le nom de l'auteur: ")
        prenom = input("Entrez le prenom de l'auteur: ")
        date_naissance = input("Entrez la date de naissance de l'auteur (YYYY-MM-DD): ")
        nationalite = input("Entrez la nationalité de l'auteur: ")

        return Auteur(nom=nom, 
                         prenom=prenom, 
                         date_naissance=date_naissance, 
                         nationalite=nationalite)
        

        