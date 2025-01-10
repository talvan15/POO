from ator import Ator

class Personagem(Ator):
    def __init__(self, nome, sexo, data_nas, contrato, caracterizacao, novela):
        super().__init__(nome, sexo, data_nas, contrato)
        self. caracterizacao = caracterizacao
        self.novela = novela
        