#ADIVINHAÇÃO DE NUMERO
import random

def acharNumero():
    numero = int(input('digite um numero: '))
    sorteado = random.randint(1,100)
    print(sorteado)
    min = 0
    max = 0
    
    while True:
        if numero == sorteado:
            print('Parabéns, você encontrou o numero! ')
            break
        else:
            if sorteado > 10 and sorteado < 90:
                print(f'QUASE!, o numero sorteado está entre {sorteado - 5} e {sorteado + 5} ')
            elif sorteado <= 10:
                min = 0
                print(f'QUASE!, o numero sorteado está entre {min} e {10} ')
            elif sorteado >= 90:
                max = 100
                print(f'QUASE!, o numero sorteado está entre {90} e {max} ')
            numero = int(input('Tente novamente: '))


            


print('TENTE ADIVINHAR O NÚMERO! ')

acharNumero()
