class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibirDetalhes(self):
        print(f"Detalhes do veículo")
        print(f"Veículo - Marca = {self.marca}, Modelo = {self.modelo}, Ano = {self.ano}")
