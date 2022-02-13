from fractions import Fraction

def isNumber(s):
    try:
        int(s)
    except ValueError:
        return False
    return True


def eval(op, u, v):
    match op:
        case "+":
            return Fraction(u) + Fraction(v)
        case "-":
            return Fraction(u) - Fraction(v)
        case "*":
            return Fraction(u) * Fraction(v)
        case "/":
            if v != 0:
                return Fraction(u) / Fraction(v)
            else:
                raise Exception
        case _:
            raise Exception


def eval_expression(expression):
    res = []

    for i in range(len(expression)):
        if isNumber(expression[i]):
            res.append(int(expression[i]))
        else:
            op = expression[i]
            try:
                right = res.pop()
                left = res.pop()
                res.append(eval(op, left, right))
            except Exception:
                return None

    if len(res) == 1:
        return res[0]
    return None


expression1 = input().split()
expression2 = input().split()

print(eval_expression(expression1) == eval_expression(expression2))
