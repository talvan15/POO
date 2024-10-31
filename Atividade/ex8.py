nome = input("Digite um nome: ")

vogais = "aeiouAEIOU"
total = 0
for i in nome:
    if i in vogais:
        total += 1

print(f'total de vogais: {total}')