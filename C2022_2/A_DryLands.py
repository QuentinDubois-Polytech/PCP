N, M = map(int, input().split())

tab = []
sum = 0
for _ in range(N):
    tab.append(list(input()))

for i in range(N):
    for j in range(M):
        if tab[i-1][j] == "#":
            sum += 1
        elif tab[i+1][j] == "#":
            sum += 1
        elif tab[i-1][j] == "#":