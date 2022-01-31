def sum_note(nbNote, notes, coef):
    res = 0
    for i in range(nbNote):
        res += notes[i] * coef[i]

    return res


nb_eleves, nb_notes = list(map(int, input().split()))
list_coef = list(map(int, input().split()))

nom_eleve, *notes_eleve = input().split()
notes_eleve = list(map(int, notes_eleve))
moyenne_eleve = sum_note(nb_notes, notes_eleve, list_coef)

for i in range(nb_eleves - 1):
    nom_eleve_read, *notes_eleve_read = input().split()
    notes_eleve_read = list(map(int, notes_eleve_read))
    moyenne_eleve_read = sum_note(nb_notes, notes_eleve_read, list_coef)

    if moyenne_eleve == moyenne_eleve_read:
        nom_eleve = "EX AEQUO"

    elif moyenne_eleve_read > moyenne_eleve:
        nom_eleve = nom_eleve_read
        moyenne_eleve = moyenne_eleve_read


print(nom_eleve)
