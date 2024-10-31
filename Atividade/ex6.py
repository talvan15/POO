#tabuada
num = int(input('Digite um numero para calcular: '))

print(f'Multiplicação:')
for i in range(1, 10 + 1):
    print(f'{num} * {i} = {num * i}')

print(f'Divisão:')
for i in range(1, 10 + 1):
    print(f'{i} / {num} = {i / num}')

print(f'Soma:')
for i in range(1, 10 + 1):
    print(f'{num} + {i} = {num + i}')

print(f'Subtração:')
for i in range(1, 10 + 1):
    print(f'{i} - {num} = {i - num}')