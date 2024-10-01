from repository.LivreRepository import LivreRepositoryList
from service.Service import Service

class LivreService(Service):
    
    def __init__(self, repository : "LivreRepositoryList"):
        self.repository = repository

    def create(self, livre):
        self.repository.save(livre)

    def show(self) -> list:
        return self.repository.select_all()

    def update(self, data: dict):
        self.repository.update(data)

    def delete(self, id: int):
        self.repository.delete(id)

