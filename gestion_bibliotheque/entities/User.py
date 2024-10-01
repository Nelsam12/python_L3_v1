class User:
    def __init__(self, nom, prenom, email, login, password):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.login = login
        self.password = password

    def afficher_info(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Email: {self.email}, Login: {self.login}"
