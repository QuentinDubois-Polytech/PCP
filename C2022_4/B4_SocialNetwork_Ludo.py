def influence(personne):
    amis = set()
    suiveur = set()
    amidami = set()
    for suiv in dico.get(personne):
        if personne in dico.get(suiv):
            amis.add(suiv)
        else:
            suiveur.add(suiv)
        for ada in dico.get(suiv):
            if not(ada in dico.get(personne)) and not(ada == personne):
                amidami.add(ada)
    return 3 * len(amis) + 2 * len(suiveur) + len(amidami)


nbpersonnes, nbrelations = map(int, input().split())

dico = {i: set() for i in range(0, nbpersonnes)}
for i in range(nbrelations):
    a, b = input().split()
    dico[int(b)].add(int(a))

#print(influence(0))
tab = [influence(i) for i in range(nbpersonnes)]
print(max(tab))