from collections import defaultdict

dict_names = defaultdict(lambda: (0, 0))
n, k = map(int, input().split())

for i in range(n):
    name = input()
    dict_names[name] = (dict_names[name][0] + 1, i)

res = sorted(((k, v) for k, v in dict_names.items()), key=lambda x: (x[1][0], x[1][1]), reverse=True)

for i in range(k):
    print(res[i][0])
