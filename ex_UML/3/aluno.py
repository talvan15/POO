from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, sexo, data_nas, matricula):
        super().__init__(nome, sexo, data_nas)
        self.matric = matricula