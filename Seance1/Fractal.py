hg = "┌"
hd = "┐"
bg = "└"
bd = "┘"

array = [[hg, hd], [bg, bd]]

def fractal_init(n):
    return fractal(n, 1, array)

def fractal(n, actual, tab):
    if n == actual:
        return tab
    else:
        new = [[] for _ in range(2**n)]
        print(tab)
        print(2**(n-1))
        for i in range(2**(n-1)):
            for j in range(2**(n-1)):
                match tab[i][j]:
                    case "┌": hg_substitution(new, i, j)
                    case "┐": hd_substitution(new, i, j)
                    case "└": bg_substitution(new, i, j)
                    case "┘": bd_substitution(new, i, j)
        return fractal(n, actual+1, new)


def hg_substitution(new, i, j):
    new[2*i].insert(j, hg)
    new[2*i].insert(j+1, hd)
    new[2*i+1].insert(j, bg)
    new[2*i+1].insert(j+1, hg)

def hd_substitution(new, i ,j):
    new[2*i].insert(j + 1, hg)
    new[2*i].insert(j + 2, hd)
    new[2*i + 1].insert(j + 1, hd)
    new[2*i + 1].insert(j + 2, bd)

def bg_substitution(new, i, j):
    new[2*i].insert(j, hg)
    new[2*i].insert(j + 1, bg)
    new[2*i + 1].insert(j, bg)
    new[2*i + 1].insert(j + 1, bd)

def bd_substitution(new, i, j):
    new[2*i].insert(j+1, bd)
    new[2*i].insert(j + 2, hd)
    new[2*i + 1].insert(j+1, bg)
    new[2*i + 1].insert(j + 2, bd)

def print_fractal(n):
    tab2 = fractal_init(n)
    print(tab2)
    for i in range(2**n):
         print("".join(tab2[i]))

#n = int(input())

# print(hg + hd + "\n" + bg + bd + "\n")
# print(hg + hd + hg + hd + "\n" +
#       bg + hg + hd + bd + "\n" +
#       hg + bg + bd + hd + "\n" +
#       bg + bd + bg + bd + "\n")

print_fractal(1)
print_fractal(2)
print_fractal(3)



