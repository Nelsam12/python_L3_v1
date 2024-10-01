class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, user):
        self.repository.save(user)

    def show(self) -> list:
        return self.repository.select_all()

    def update(self, user):
        self.repository.update(user)

    def delete(self, user_id):
        self.repository.delete(user_id)
