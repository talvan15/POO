list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print (list[1:9])
print (list[8:13])

pares = [num for num in list if num % 2 == 0]
print(f'pares: {pares}')

impares = [num for num in list if num % 2 != 0]
print(f'Impares: {impares}')

multiplos = [num for num in list if num % 2 == 0 or num % 3 == 0 or num % 4 == 0]

print(f'multiplos de 2, 3, 4: {multiplos}')
 
soma1 = sum(list[10:15])
soma2 = sum(list[3:9])
razao = soma1 / soma2
print(f'Razão: {razao}')

list.reverse()
print(f'lista reversa: {list}')
