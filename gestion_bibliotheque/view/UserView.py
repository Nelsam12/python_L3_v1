from tabulate import tabulate

from entities.User import User
from service.UserService import UserService

def get_user_infos(users_data):
    users_for_display = []
    for user in users_data:
        user_copy = {
            "nom": user["nom"],
            "prenom": user["prenom"],
            "email": user["email"],
            "login": user["login"],
            # Don't display the password for security reasons
        }
        users_for_display.append(user_copy)

    headers = ["Nom", "Prénom", "Email", "Login"]
    rows = [[user["nom"], user["prenom"], user["email"], user["login"]] for user in users_for_display]
    
    return rows, headers

class UserView:
    def __init__(self, user_service: "UserService"):
        # Dependency injection
        self.user_service = user_service

    def create(self) -> "User":
        nom = input("Entrez le nom de l'utilisateur: ")
        prenom = input("Entrez le prénom de l'utilisateur: ")
        email = input("Entrez l'email de l'utilisateur: ")
        login = input("Entrez le login de l'utilisateur: ")
        password = input("Entrez le mot de passe de l'utilisateur: ")
        return User(nom, prenom, email, login, password)

    def select_all_for_display(self):
        return get_user_infos(self.user_service.show())
      
       
