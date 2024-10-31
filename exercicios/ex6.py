# Definir se um numero é primo
num = int(input('Digite um numero: '))
contador = 0

for numeros in range(1, num + 1):
    if num % numeros == 0:
        contador += 1

if contador > 2:
    print(f'O numero {num} não é primo! ')

else:
    print(f'O numero {num} é primo! ')