num = int(input('Digite um numero inteiro positivo: '))

if num < 0:
    print('O numero digitado é negativo')

else:
    soma = sum(int(digito) for digito in str(num))

print(f'A soma dos digitos é {soma} ')