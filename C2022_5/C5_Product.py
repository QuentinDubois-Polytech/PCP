N, R, P = map(int, input().split())
L = list(map(int, input().split()))
calcul = [(1, 0)]

IS_ZERO = -1
count = 0

for i in range(0, N):
    if L[i] == 0:
        count += 1
        calcul.append((1, IS_ZERO))
    else:
        calcul.append(((L[i] * calcul[i][0]) % P, count))

for _ in range(R):
    a, b = map(int, input().split())

    if calcul[a+1][1] != calcul[b+1][1] or calcul[a+1][1] == IS_ZERO or calcul[b+1][1] == IS_ZERO:
        print(0)
    else:
        print((calcul[b+1][0] * pow(calcul[a][0], P-2, P)) % P)
