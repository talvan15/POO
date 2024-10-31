#Primeira forma
nome = input('Digite um nome: ')

contador = 0
for letras in nome:
    if letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u":
        contador += 1
print(f'Existem {contador} vogais na palavra ')


# Segunda forma (Mais "correto")
#definir uma variavel com as vogais para comparar:
nome = input('Digite um nome: ')
vogais = 'aeiouAEIOU'
contador = 0
for letras in nome:
    if letras in vogais:
        contador += 1

print(f'Existem {contador} vogais na palavra {nome}')