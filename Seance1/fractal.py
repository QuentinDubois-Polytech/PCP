hg = "┌"
hd = "┐"
bg = "└"
bd = "┘"

def fractal(n):
    if n == 1:
        tab = [[] for _ in range(2)]
        tab[0][0] = hg
        tab[0][1] = hd
        tab[1][0] = bg
        tab[1][1] = bd

    elif n == 2:
        print(hg + hd + hg + hd + "\n" +
              bg + hg + hd + bd + "\n" +
              hg + bg + bd + hd + "\n" +
              bg + bd + bg + bd + "\n")
    else:
        res = ""
        for i in range(2*n):
            res

#n = int(input())

print(hg + hd + "\n" + bg + bd + "\n")
print(hg + hd + hg + hd + "\n" +
      bg + hg + hd + bd + "\n" +
      hg + bg + bd + hd + "\n" +
      bg + bd + bg + bd + "\n")



