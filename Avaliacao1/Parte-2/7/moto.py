from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipoGuidao):
        super().__init__(marca, modelo, ano)
        self.guidao = tipoGuidao

    def exibirDetalhes(self):
        print(f"Moto - Marca = {self.marca}, Modelo = {self.modelo}, Ano = {self.ano}, Portas = {self.guidao}")
