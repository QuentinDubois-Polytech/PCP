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
        len = 2**actual
        new = [[] for _ in range(len*2)]
        for i in range(len):
            for j in range(len):
                match tab[i][j]:
                    case "┌": hg_substitution(new, i, j)
                    case "┐": hd_substitution(new, i, j)
                    case "└": bg_substitution(new, i, j)
                    case "┘": bd_substitution(new, i, j)
        return fractal(n, actual+1, new)


def hg_substitution(new, i, j):
    new[2*i].append(hg)
    new[2*i].append(hd)
    new[2*i+1].append(bg)
    new[2*i+1].append(hg)

def hd_substitution(new, i ,j):
    new[2*i].append(hg)
    new[2*i].append(hd)
    new[2*i + 1].append(hd)
    new[2*i + 1].append(bd)

def bg_substitution(new, i, j):
    new[2*i].append(hg)
    new[2*i].append(bg)
    new[2*i + 1].append(bg)
    new[2*i + 1].append(bd)

def bd_substitution(new, i, j):
    new[2*i].append(bd)
    new[2*i].append(hd)
    new[2*i + 1].append(bg)
    new[2*i + 1].append(bd)

def print_fractal(n):
    res = ""
    tab = fractal_init(n)
    for elem in tab:
         res += "".join(elem) + '\n'
    print(res)


print_fractal(int(input()))




