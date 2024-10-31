import random
lista = ['jose', 'maria', 'joao', 'fernando', 'ana', 'joana', 'bartô', 'junior','ed', 'francisca']

while lista:
    sortear = random.choice(lista)
    print(lista)
    print(sortear)
    lista.remove(sortear)
    random.shuffle(lista)
    

    
