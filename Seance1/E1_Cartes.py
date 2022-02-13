list_cout = []

def recursion(n, list_cartes, nb_cout):
    global list_cout

    i = 0
    while list_cartes[i][0] == i+1 and list_cartes[i][1] == "R":
        if i == n - 1:
            return nb_cout
        i+=1

    for nb_cartes_retourner in range(1, n + 1):
        retourner_cartes(n, list_cartes, nb_cartes_retourner)
        list_cout.append(recursion(n, retourner_cartes(n, list_cartes,  nb_cartes_retourner), nb_cout+1))
        retourner_cartes(n, list_cartes, nb_cartes_retourner)


def retourner_cartes(n, list_cartes, nb_cartes_retourner):
    for i in range(int(nb_cartes_retourner/2)):
        permuter(n - nb_cartes_retourner + i, n-1-i, list_cartes)
    return list_cartes


def permuter(i, j, list_cartes):
    list_cartes[i] = (list_cartes[i][0], "R") if list_cartes[i][1] == "V" else (list_cartes[i][0], "V")
    list_cartes[j] = (list_cartes[j][0], "R") if list_cartes[j][1] == "V" else (list_cartes[j][0], "V")

    tmp = list_cartes[i]
    list_cartes[i] = list_cartes[j]
    list_cartes[j] = tmp

    return list_cartes


n = int(input())
data = input().split()

list_cartes = []
for i in range(n):
    list_cartes.append((int(data[2*i]), data[2*i+1]))

recursion(n, list_cartes, 0)
print(min(list_cartes))

# print(retourner_cartes(7, list_cartes, 5))
