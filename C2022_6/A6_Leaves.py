N = int(input())

voisins = {}

for i in range(1, N+1):
    voisins[i] = set()

for _ in range(N-1):
    a, b = map(int, input().split())
    voisins[a].add(b)
    voisins[b].add(a)

res = 0
for key in voisins:
    if len(voisins[key]) <= 1:
        res += 1

print(res)
