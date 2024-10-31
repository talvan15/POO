tam = int (input('total de numeros: '))
soma = 0
for i in range(1,tam + 1):
    cont = int(input(f'Numero {i}: '))
    soma += cont

print(f'Soma dos numeros: {soma}')