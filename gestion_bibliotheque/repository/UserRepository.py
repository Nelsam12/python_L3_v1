
import json
import os

class UserRepository:
    def __init__(self, filename="./db/json/users.json"):
        self.filename = filename
        # If the file does not exist, create it with an empty list as initial content
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def _load_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def save(self, user):
        data = self._load_data()
        user_dict = user.__dict__
        user_dict['id'] = len(data) + 1  # Generate a new ID
        data.append(user_dict)
        self._save_data(data)

    def update(self, user):
        data = self._load_data()
        for idx, item in enumerate(data):
            if item['id'] == user.id:
                data[idx] = user.__dict__
                self._save_data(data)
                return
        raise ValueError(f"User with id {user.id} not found.")

    def delete(self, user_id):
        data = self._load_data()
        new_data = [item for item in data if item['id'] != user_id]
        if len(new_data) == len(data):
            raise ValueError(f"User with id {user_id} not found.")
        self._save_data(new_data)

    def select_all(self):
         return self._load_data()

    def select_by_id(self, user_id):
        data = self._load_data()
        for item in data:
            if item['id'] == user_id:
                return User(**item)
        raise ValueError(f"User with id {user_id} not found.")
