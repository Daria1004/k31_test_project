

class Customer:
    id: int
    token: str

    def __init__(self, id, token):
        self.id = id
        self.token = token

    def get_id(self):
        return self.id

    def get_token(self):
        return self.token
