N = int(input())

voisins = {}
d = []

for i in range(1, N+1):
    voisins[i] = set()

for _ in range(N-1):
    a, b = map(int, input().split())
    voisins[a].add(b)
    voisins[b].add(a)

is_leaf = [[] for _ in range(N)]

for i in range(1, N+1):
    taille = len(voisins[i])
    d.append(taille)
    if taille <= 1:
        is_leaf[0].append(i)

rayon = 0

while len(is_leaf[rayon]) >= 2:
    for i in is_leaf[rayon]:
        for j in voisins[i]:
            d[j - 1] -= 1
            if d[j-1] == 1:
                is_leaf[rayon + 1].append(j)
    rayon += 1


print(rayon)

if len(is_leaf[rayon]) == 1:
    print(is_leaf[rayon][0])
else:
    center = is_leaf[rayon - 1]
    center.sort()
    print(center[0], center[1])



