N, R, P = map(int, input().split())
L = list(map(int, input().split()))
calcul = []

count = 0

if L[0] == 0:
    calcul.append((1, -1))
else:
    calcul.append((L[0], count))

for i in range(1, N):
    if L[i] == 0:
        count += 1
        calcul.append((1, -1))
    else:
        if L[i-1] == 0:
            calcul.append((L[i], count))
        else:
            calcul.append(((L[i] * calcul[i-1][0]) % P, count))

for _ in range(R):
    a, b = map(int, input().split())

    if calcul[a][1] != calcul[b][1] or calcul[a][1] == -1 or calcul[b][1] == -1:
        print(0)
    else:
        if a == 0:
            print(calcul[b][0])
        else:
            print((calcul[b][0] * pow(calcul[a-1][0], P-2, P)) % P)
