# Valeurs de player
# 0 : deuxième joueur à la SG
# 1 : premier joueur à la SG

def division(number, player):
    if number == 0:
        return 1 - player
    else:
        number -= 1
        if player == 0:
            return min(
                division(number//2, 1),
                division(number//3, 1),
                division(number//7, 1)
            )
        else:
            return max(
                division(number // 2, 0),
                division(number // 3, 0),
                division(number // 7, 0)
            )

def print_winner(number):
    res = division(number, 0)
    print("First player" if res == 0 else "Second player")


n = int(input())
print_winner(n)