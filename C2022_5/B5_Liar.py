def contradiction(i, j):
    return (L[i][0] == L[j][0] and L[i][1] != L[j][1]) or (L[i][0] != L[j][0] and L[i][1] == L[j][1]) or (
                L[i][0] != L[j][0] and L[i][1] == L[j][1])

N = int(input())

L = []

for i in range(N):
    a, b = tuple(input().split())
    L.append((int(a), float(b)))

L.sort(key=lambda x: x[0])

for i in range(0, N-1):
    if contradiction(i, i+1):
        if i + 2 >= N-1:
            break
        elif i - 1 < 0:
            continue
        elif contradiction(i, i+2):
            print(i+1)
            exit(0)

        elif contradiction(i+1, i-1):
            print(i+1)
            exit(0)
print(0)






