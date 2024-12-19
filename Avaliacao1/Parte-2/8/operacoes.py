from abc import ABC, abstractmethod

class Operacoes(ABC):
    @abstractmethod
    def adicionar(self, item):
        pass

    @abstractmethod
    def remover(self, item):
        pass
