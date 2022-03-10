nb_personnes, nb_relations = map(int, input().split())

relation = {}
res = 0

for p in range(nb_personnes):
    relation[p] = set()

for _ in range(nb_relations):
    a, b = map(int, input().split())
    relation[b].add(a)

for p1 in range(nb_personnes):
    suiveurs = set()
    amis = set()
    suiveurs_amis = set()

    for p2 in relation[p1]:
        if p1 in relation[p2]:
            amis.add(p2)
            for p3 in relation[p2]:
                if p3 not in relation[p1] and p3 != p1:
                    suiveurs_amis.add(p3)
        else:
            suiveurs.add(p2)

    value = 3 * len(amis) + 2 * len(suiveurs) + len(suiveurs_amis)
    if value > res:
        res = value

print(res)



