from entities.Auteur import Auteur
from entities.Livre import Livre
from repository.UserRepository import UserRepository
from repository.LivreRepository import LivreRepositoryJson
from repository.Repository import Repository
from service.UserService import UserService
from view.AuteurView import AuteurView
from view.LivreView import LivreView
from service.LivreService import LivreService
from view.UserView import UserView
from view.View import View


def menu():
    print("--- Menu ---")
    print("1. Créer un livre")
    print("2. Afficher les Livres ")
    print("3. Créer Utilisateur ")
    print("4. Afficher les utilisateurs ")
    print("5. Quitter")
    return int(input("Votre choix : "))




if __name__ == "__main__":
    # Creation des Repository
    # auteur_repository = AuteurRepositoryList()
    livre_repository = LivreRepositoryJson()

    # Creation des Services
    # auteur_service = AuteurService(auteur_repository)
    livre_service = LivreService(livre_repository) 

    # Création des Views
    auteur_view = AuteurView()
    livre_view = LivreView(auteur_view, livre_service)

    # Create the UserRepository and UserService
    user_repository = UserRepository()
    user_service = UserService(user_repository)

    # Create the UserView
    user_view = UserView(user_service)

    while True:
        choix = menu()
        match (choix):
            case 1:
                livre = livre_view.create()
                livre_service.create(livre)
                print("Livre créé avec succès.")
                
            case 2:
               
                header  = livre_view.select_all_for_display()[1]
                livres  = livre_view.select_all_for_display()[0]
                # print(livres)
                View.afficher(livres, header)
               
            case 3:
                user = user_view.create()  # Create a new user
                user_service.create(user)
                print("User créé avec succès.")
                
            case 4:
               
                header  = user_view.select_all_for_display()[1]
                users  = user_view.select_all_for_display()[0]
                # print(livres)
                View.afficher(users, header)
               
           

            case 5:
                exit()
                print("Merci d'avoir utilisé notre application.")


            case _:
                print("Choix invalide. Veuillez réessayer.")


  

    