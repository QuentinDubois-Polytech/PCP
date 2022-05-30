N = int(input())

values = list(map(int, input().split()))
values.sort(reverse=True)
print(values)

to_add = 0
first = True
k = 0
if N % 2 == 0:
    k = 2
else:
    k = 3

if len(values) > 3:
    res = 0
    for i in range(k):
        res += values.pop()
    values.append(res)
    to_add += res
    values.sort(reverse=True)

while len(values) > 3:
    res = 0
    for i in range(3):
        res += values.pop()
    values.append(res)
    to_add += res
    values.sort(reverse=True)

values.append(to_add)
print(sum(values))

