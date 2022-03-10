dico = {'#': 0, '.': 1}

height, width = map(int, input().split())
tab = [[dico[i] for i in input()] for _ in range(height)]

res = 0

for i in range(height):
    for j in range(width):
        if tab[i][j]:
            res = 1
            break
    if res == 1:
        break

for i in range(1, height):
    for j in range(2, width):
        if tab[i][j] != 0:
            tab[i][j] = min(tab[i][j-1], tab[i][j-2], tab[i-1][j-1]) + 1

        if res < tab[i][j]:
            res = tab[i][j]

print(res)

