#ADIVINHAÇÃO DE NUMERO
import random

def acharNumero():
    numero = int(input('digite um numero: '))
    sorteado = random.randint(1,100)
    print(sorteado)
    
    while True:
        if numero == sorteado:
            print('Parabéns, você encontrou o numero! ')
            break
        else:
            if numero > sorteado:
                print(f'QUASE!, o numero sorteado é menor. ')
            elif numero < sorteado:
                print(f'QUASE!, o numero sorteado é maior! ')

            numero = int(input('Tente novamente: '))


print('TENTE ADIVINHAR O NÚMERO! ')

acharNumero()