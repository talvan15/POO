from datetime import datetime
class Usuario:
    def __init__(self, id, nome, login, senha):
        self._id = id
        self._nome = nome
        self._login = login
        self._senha = senha

    def autenticar(self, login, senha):
        return self._login == login and self._senha == senha



        