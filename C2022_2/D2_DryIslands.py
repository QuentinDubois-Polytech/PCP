# True = Terre
# False = Mer

N, M = map(int, input().split())
tab = [[] for _ in range(N+2)]
res = [[] for _ in range(N)]

sum = 0

tab[0] = [True] * (M+2)
tab[N+1] = [True] * (M+2)

for i in range(N):
    data = list(input())
    tab[i + 1].append(True)
    for elem in data:
        tab[i + 1].append(False if elem == "#" else True)
    tab[i + 1].append(True)

for i in range(1, N+1):
    for j in range(1, M+1):
        if tab[i][j] and tab[i - 1][j - 1] and tab[i - 1][j] and tab[i - 1][j + 1] \
                and tab[i][j - 1] and tab[i][j + 1] \
                and tab[i + 1][j - 1] and tab[i + 1][j] and tab[i + 1][j + 1]:
            res[i - 1].insert(j-1, True)
        else:
            res[i - 1].insert(j-1, False)

print(res)