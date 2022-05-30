n, d = map(int, input().split())
parcours = [list(map(int, input().split())) for _ in range(d)]
list_min = [0, parcours[0][0]]

for i in range(2, n):
    list_min.append(min((list_min[i - j - 1] + parcours[j][i - j - 1] for j in range(min(i, d)))))

print(list_min[n - 1])
