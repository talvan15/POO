class carros:
    def __init__(self, marca, modelo, velocidade_atual, velocidade_maxima, tanque_combustivel, consumo_combustivel):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima
        self.tanque_combustivel = tanque_combustivel
        self.consumo_combustivel = consumo_combustivel
    
    def acelerar(self):
        velocidade = 2
        for _ in range(self.velocidade_maxima):
            self.velocidade_atual += velocidade
            print(self.velocidade_atual)

            if self.velocidade_atual >= self.velocidade_maxima:
                print(f'O carro atingiu a velocidade máxima de {self.velocidade_maxima} ')
                break

    def frear(self, quantidade):
        nova_velocidade = self.velocidade_atual - quantidade
        if nova_velocidade < 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual = nova_velocidade
        print(f'{self.marca} {self.modelo} reduziu a velocidade para {self.velocidade_atual} km/h')

    def abastecer(self, litros):
        self.tanque_combustivel += litros
        print(f'{self.marca} {self.modelo} foi abastecido com {litros} litros. Combustível atual: {self.tanque_combustivel} litros')

    def dirigir(self, distancia):
        combustivel_necessario = distancia * self.consumo_combustivel
        if combustivel_necessario > self.tanque_combustivel:
            print(f'{self.marca} {self.modelo} ficou sem combustível após percorrer {self.tanque_combustivel / self.consumo_combustivel:.2f} km')
            self.distancia_percorrida += self.tanque_combustivel / self.consumo_combustivel
            self.tanque_combustivel = 0
            self.velocidade_atual = 0
        else:
            self.distancia_percorrida += distancia
            self.tanque_combustivel -= combustivel_necessario
            print(f'{self.marca} {self.modelo} percorreu {distancia} km. Combustível restante: {self.tanque_combustivel:.2f} litros')

    def verificar_combustivel(self):
        return self.tanque_combustivel

    def status(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Velocidade Atual: {self.velocidade_atual} km/h, Combustível Restante: {self.tanque_combustivel:.2f} litros, Distância Percorrida: {self.distancia_percorrida:.2f} km')


class Corrida:
    def __init__(self, distancia_total):
        self.carros = []
        self.distancia_total = distancia_total
        self.vencedor = None

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def iniciar_corrida(self):
        while True:
            carros_em_movimento = [carro for carro in self.carros if carro.verificar_combustivel() > 0]
            if len(carros_em_movimento) == 0:
                print('Todos os carros ficaram sem combustível.')
                break

            for carro in carros_em_movimento:
                carro.acelerar(10)  # Acelera em 10 km/h como exemplo
                carro.dirigir(carro.velocidade_atual / 10)  # Dirige proporcionalmente à velocidade

                if carro.distancia_percorrida >= self.distancia_total:
                    self.vencedor = carro
                    print(f'O vencedor é {carro.marca} {carro.modelo}!')
                    return

    def resultado_corrida(self):
        if self.vencedor:
            print(f'O carro vencedor é {self.vencedor.marca} {self.vencedor.modelo}, percorrendo a distância total de {self.distancia_total} km.')
        else:
            print('Nenhum vencedor, todos os carros ficaram sem combustível.')


# Exemplo de uso
carro1 = carros("Ferrari", "F8", 340, 50, 0.1)
carro2 = carros("Lamborghini", "Aventador", 350, 60, 0.12)

corrida = Corrida(100)  # Distância total de 100 km
corrida.adicionar_carro(carro1)
corrida.adicionar_carro(carro2)
corrida.iniciar_corrida()
corrida.resultado_corrida()


                
    
