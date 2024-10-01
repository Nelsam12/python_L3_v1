from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def select_all(self):
        pass

    @abstractmethod
    def select_by_id(self, id):
        pass