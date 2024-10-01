class Auteur:
    def __init__(self, nom : str, prenom : str, date_naissance : str, nationalite : str):
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__nationalite = nationalite
    
    def afficher_info(self):
        return f"Nom: {self.__nom}\nPrenom: {self.__prenom}\nDate de naissance: {self.__date_naissance}\nNationalité: {self.__nationalite}"
    

    # GETTERS
    def get_nom(self) -> str:
        return self.__nom
    
    def get_prenom(self) -> str:
        return self.__prenom
    
    def get_date_naissance(self) -> str:
        return self.__date_naissance
    
    def get_nationalite(self) -> str:
        return self.__nationalite
    
    # SETTERS

    def set_nom(self, nom : str):
        self.__nom = nom

    def set_prenom(self, prenom : str):
        self.__prenom = prenom

    def set_date_naissance(self, date_naissance : str):
        self.__date_naissance = date_naissance

    def set_nationalite(self, nationalite : str):
        self.__nationalite = nationalite

    