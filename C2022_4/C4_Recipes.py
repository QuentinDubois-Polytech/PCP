def formulaX(state, nb):
    x = (state[0] + state[1]) % nb
    y = (state[1] + state[2]) % nb
    z = (state[2] + state[0]) % nb
    return x, y, z


def formulaY(state, nb):
    x = (state[0] + 1) % nb
    y = (state[1] - 1) % nb
    z = state[2]
    return x, y, z


def formulaZ(state):
    x = state[2]
    y = state[1]
    z = state[0]
    return x, y, z


def append_elem(stack, value):
    if value not in states_achieved:
        stack.append(value)
        states_achieved.add(value)


def treatment(origin, dest):
    while origin:
        value = origin.pop()
        append_elem(dest, formulaX(value, N))
        append_elem(dest, formulaY(value, N))
        append_elem(dest, formulaZ(value))


def end_achieved():
    if res in states_achieved:
        print(count)
        exit(0)


def main():
    global count
    stack1 = [init]
    stack2 = []

    if res == init:
        print(count)
    else:
        while True:
            treatment(stack1, stack2)
            count += 1
            end_achieved()

            treatment(stack2, stack1)
            count += 1
            end_achieved()


N, a, b, c = map(int, input().split())
res = tuple(map(int, input().split()))
init = (a, b, c)
states_achieved = {init}
count = 0

main()
