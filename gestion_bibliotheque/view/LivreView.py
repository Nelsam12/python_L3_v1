
from entities.Livre import Livre
from entities.Auteur import Auteur
from service.LivreService import LivreService
from view.AuteurView import AuteurView


def get_livre_infos(livres_data):
    livres_for_display = []
    for livre in livres_data:
        # Create a copy of the livre dictionary without the 'auteur' field
        livre_copy = {
            "titre": livre["_Livre__titre"],
            "annee_edition": livre["_Livre__annee_edition"],
            "genre": livre["_Livre__genre"],
            "etat": livre["_Livre__etat"],
            "exemplaire": livre["_Livre__exemplaire"],
        }
        livres_for_display.append(livre_copy)
    rows = [[livre["titre"], livre["annee_edition"], livre["genre"], livre["etat"], livre["exemplaire"]] for livre in livres_for_display]
    headers = ["Titre", "Année d'Édition", "Genre", "État", "Exemplaires"]
    return [rows,headers]
            

class LivreView:
    def __init__(self, auteur_view : "AuteurView", livre_service: "LivreService"):
        # Injection de dépendance
        self.auteur_view = auteur_view
        self.livre_service = livre_service
        
    def create(self) -> "Livre":
        titre = input("Entrez le titre du livre: ")
        annee_edition = input("Année d'édition : ")
        genre = input("Genre : ")
        etat = "DISPONIBLE"
        # etat = input("Etat (DISPONIBLE, INDISPONIBLE EMPRUNTÉ) : ")
        auteur = self.auteur_view.create()
        exemplaire = 100  
        # exemplaire = int(input("Entrer le nombre d'exemplaire : "))
        return Livre(titre, auteur, annee_edition, genre, etat, exemplaire)
    
    def select_all_for_display(self) -> list:
        return get_livre_infos(self.livre_service.show())