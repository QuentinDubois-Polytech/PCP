from collections import defaultdict


def dicho(vrai, faux):
    while faux - vrai != 1:
        milieu = (vrai + faux) // 2
        if cmp(milieu):
            vrai = milieu
        else:
            faux = milieu

    print(vrai)

def cmp(taille):
    res = 0
    i = 0

    hash_table = defaultdict(list)
    for j in range(i, taille):
        res = (res * 26 + alphabet[chaine[j]]) % p
    hash_table[res].append(i)

    while i < (length - taille):
        res -= pow(26, taille - 1, p) * alphabet[chaine[i]]
        res = (res * 26 + alphabet[chaine[taille + i]]) % p

        hash_table[res].append(i + 1)
        if len(hash_table.get(res)) == 3:
            return True

        i += 1

    return False


chaine = input()

length = len(chaine)
alphabet = {}
p = pow(2, 61) - 1

value = 0
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet.setdefault(i, value)
    value += 1

dicho(0, length)
