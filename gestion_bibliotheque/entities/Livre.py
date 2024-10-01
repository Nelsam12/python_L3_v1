from entities.Auteur import Auteur
class Livre:
    def __init__(self, titre : str, auteur : "Auteur", annee_edition : int, genre : str, etat : str, exemplaire : int):
        self.__titre = titre
        self.__auteur = auteur
        self.__annee_edition = annee_edition
        self.__genre = genre
        self.__etat = etat
        self.__exemplaire = exemplaire

    def afficher_info(self):
        return f"Titre: {self.__titre}\nAuteur: {self.__auteur.afficher_info()}\nAnnée d'édition: {self.__annee_edition}\nGenre: {self.__genre}\nEtat : {self.__etat}\nExemplaire : {self.__exemplaire}"
    

    # GETTERS
    def get_titre(self) -> str:
        return self.__titre
    
    def get_auteur(self) -> "Auteur":
        return self.__auteur
    
    def get_annee_edition(self) -> int:
        return self.__annee_edition
    
    def get_genre(self) -> str:
        return self.__genre
    
    def get_etat(self) -> str:
        return self.__etat
    
    def get_exemplaire(self) -> int:
        return self.__exemplaire
    

    # SETTERS
    
    def set_titre(self, titre : str):
        self.__titre = titre

    def set_auteur(self, auteur : "Auteur"):
        self.__auteur = auteur

    def set_annee_edition(self, annee_edition : int):
        self.__annee_edition = annee_edition

    def set_genre(self, genre : str):
        self.__genre = genre

    def set_etat(self, etat : str):
        self.__etat = etat

    def set_exemplaire(self, exemplaire : int):
        self.__exemplaire = exemplaire

    