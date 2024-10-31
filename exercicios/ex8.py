#Crie um programa que peça ao usuário um número e depois exiba todos os números primos até esse número.
num = int(input('Digite um numero '))

contador = 0
for i in num:
    control = i
    for j in control:
        if i % j == 0:
            contador += 1
        if contador == 2:
            print(f'{control} é primo! ')

    control = 0
