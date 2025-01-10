from datetime import datetime

class Postagem:
    def __init__(self, id, titulo, texto, dataPublicacao):
        self._id = id
        self._titulo = titulo
        self._texto = texto
        self._dataPublicacao = dataPublicacao

    def publicacao(self):
        return datetime.now() >= self._dataPublicacao
  