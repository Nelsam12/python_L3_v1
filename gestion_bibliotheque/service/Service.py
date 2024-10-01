from abc import abstractmethod
class Service():
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def show(self) -> list:
        pass

    @abstractmethod
    def update(self, data: dict):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass