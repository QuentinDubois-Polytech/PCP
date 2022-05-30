n, m = map(int, input().split())

list_num = [list(map(lambda x: int(x, 16), input().split()))]

for i in range(1, n.bit_length()):
    shift_elem = 2 ** (i-1)
    list_num.append([list_num[i-1][j] | list_num[i-1][j + shift_elem] for j in range(n - 2*shift_elem + 1)])

for j in range(m):
    start, end = map(int, input().split())
    power_2_cmp = (end + 1 - start).bit_length() - 1
    print(f"{list_num[power_2_cmp][start] | list_num[power_2_cmp][end - 2 ** power_2_cmp + 1]:X}")
