list = input().split()
lumino_list = []

nb_elem = 0
for elem in list:
    R = int(elem[1:3], 16)
    G = int(elem[3:5], 16)
    B = int(elem[5:7], 16)
    lumino_list.append((R, G, B))
    nb_elem += 1

lumino_list.sort(key=lambda e: 0.2126*e[0] + 0.7152*e[1] + 0.0722*e[2])

elem_found = lumino_list[nb_elem // 2]
R = elem_found[0]
G = elem_found[1]
B = elem_found[2]

print(f"#{R:02X}{G:02X}{B:02X}")
