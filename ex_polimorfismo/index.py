class Animal:
    def emitirSom(self):
        pass

class Cachorro(Animal):
    def emitirSom(self):
        print("Au Au")

class Gato(Animal):
    def emitirSom(self):
        print("Miau")

class Vaca(Animal):
    def emitirSom(self):
        print("Muuuu")


def fazer_barulho():
    animais = [Cachorro(), Gato(), Vaca()]

    for item in animais:
        item.emitirSom()

fazer_barulho()