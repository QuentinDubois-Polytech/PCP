# Valeurs de player
# True : premier joueur
# False : deuxième joueur

def division(number, divide_by, player):
    if not player:
        if (number - 1) // 2 == 0 or (number - 1) // 3 == 0 or (number - 1) // 7 == 0:
            return False

    number = (number - 1) // divide_by

    if number == 0:
        return player
    else:
        return division(number, 2, not player) or division(number, 3, not player) or division(number, 7, not player)


def print_winner(number):
    res = division(number, 2, True) or division(number, 3, True) or division(number, 7, True)
    print("First player" if res else "Second player")


n = int(input())
print_winner(n)