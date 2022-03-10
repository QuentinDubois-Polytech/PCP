import re

nb_lines, nb_columns = map(int, input().split())
word = input()

tab = []
nb = 0

for _ in range(nb_lines):
    tab.append(input())

tab_transposed = [[tab[i][j] for i in range(nb_lines)] for j in range(nb_columns)]
word_reversed = ''.join(reversed(word))

for i in range(nb_lines):
    nb += \
        len(re.findall("(?=" + word +")", tab[i])) \
        + len(re.findall("(?=" + word_reversed + ")", tab[i]))

for i in range(nb_columns):
    nb += \
        len(re.findall("(?=" + word + ")", ''.join(tab_transposed[i]))) \
        + len(re.findall("(?=" + word_reversed + ")", ''.join(tab_transposed[i])))

print(nb)
