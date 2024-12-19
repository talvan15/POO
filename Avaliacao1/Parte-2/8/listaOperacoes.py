from operacoes import Operacoes

class ListaOperacoes(Operacoes):
    def __init__(self):
        self.lista = []

    def adicionar(self, item):
        self.lista.append(item)
        print(f"Item {item} adicionado.")

    def remover(self, item):
        if item in self.lista:
            self.lista.remove(item)
            print(f"Item {item} removido.")
        else:
            print(f"Item {item} não encontrado na lista.")

    def exibir(self):
        print(f"Lista atual: {self.lista}")