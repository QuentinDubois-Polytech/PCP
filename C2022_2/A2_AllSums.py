def pre_sum(tab, taille):
    list_res = [tab[0]]
    for i in range(1, taille):
        list_res.append(list_res[i - 1] + tab[i])
    return list_res


S, N = map(int, input().split())
numbers = list(map(int, input().split()))
pre_calcul = pre_sum(numbers, S)
list_res = []

for _ in range(N):
    start, end = map(int, input().split())

    if start == 0:
        list_res.append(pre_calcul[end])
    else:
        list_res.append(pre_calcul[end] - pre_calcul[start-1])

for i in range(N):
    print(list_res[i])
