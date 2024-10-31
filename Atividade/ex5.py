#fibonacci
termo1 = 0
termo2 = 1

print(termo1, termo2, end=" ")

for i in range(2,10):
    termo = termo1 + termo2
    print(termo, end=" ")

    termo1 = termo2
    termo2 = termo
