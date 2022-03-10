N, M = map(int, input().split())
tab = [[] for _ in range(N + 2)]
map = [[] for _ in range(N + 2)]
sum = 0

tab[0] = [True] * (M + 2)
tab[N + 1] = [True] * (M + 2)

map[0] = [True] * (M + 2)
map[N + 1] = [True] * (M + 2)
stack = []

for i in range(N):
    data = list(input())
    tab[i + 1].append(True)
    for elem in data:
        tab[i + 1].append(False if elem == "#" else True)
    tab[i + 1].append(True)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if tab[i][j] and tab[i - 1][j - 1] and tab[i - 1][j] and tab[i - 1][j + 1] \
                and tab[i][j - 1] and tab[i][j + 1] \
                and tab[i + 1][j - 1] and tab[i + 1][j] and tab[i + 1][j + 1]:
            map[i][j] = True
        else:
            map[i][j] = False

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if map[i][j]:
            stack = [(i, j)]
            while len(stack) > 0:
                x, y = stack.pop()
                sum += 1
                map[i][j] = False
                if map[x - 1][y]:
                    stack.append((x - 1, y))
                if map[x + 1][y]:
                    stack.append((x + 1, y))
                if map[i][j - 1]:
                    stack.append((x, y - 1))
                if map[i][j + 1]:
                    stack.append((x, y + 1))

print(sum)
