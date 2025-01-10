from pessoa import Pessoa

class Ator(Pessoa):
    def __init__(self, nome, sexo, data_nas, contrato):
        super().__init__(nome, sexo, data_nas)
        self.contrato = contrato
