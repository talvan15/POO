from datetime import date

class Contrato:
    def __init__(self, inicio: date, fim: date, salario: float):
        self.inicio = inicio
        self.fim = fim
        self.salario = salario