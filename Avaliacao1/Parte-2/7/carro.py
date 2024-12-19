from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numeroPortas):
        super().__init__(marca, modelo, ano)
        self.numeroPortas = numeroPortas

    def exibirDetalhes(self):
        print(f"Carro - Marca = {self.marca}, Modelo = {self.modelo}, Ano = {self.ano}, Portas = {self.numeroPortas}")
