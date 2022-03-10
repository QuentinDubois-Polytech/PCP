N, a, b, c = map(int, input().split())
res = tuple(map(int, input().split()))
init = (a, b, c)
states_achieved = {init}


count = 0

stack1 = [init]
stack2 = []

if res == init:
    print(count)
    exit(0)

while True:
    while stack1:
        value = stack1.pop()
        value1 = ((value[0] + value[1]) % N, (value[1] + value[2]) % N, (value[2] + value[0]) % N)
        if value1 not in states_achieved:
            stack2.append(value1)
            states_achieved.add(value1)

        value2 = ((value[0] + 1) % N, (value[1] - 1) % N, value[2])
        if value2 not in states_achieved:
            stack2.append(value2)
            states_achieved.add(value2)

        value3 = (value[2], value[1], value[0])
        if value3 not in states_achieved:
            stack2.append(value3)
            states_achieved.add(value3)

    count += 1

    if res in states_achieved:
        print(count)
        exit(0)


    while stack2:
        value = stack2.pop()

        value1 = ((value[0] + value[1]) % N, (value[1] + value[2]) % N, (value[2] + value[0]) % N)
        if value1 not in states_achieved:
            stack1.append(value1)
            states_achieved.add(value1)

        value2 = ((value[0] + 1) % N, (value[1] - 1) % N, value[2])
        if value2 not in states_achieved:
            stack1.append(value2)
            states_achieved.add(value2)

        value3 = (value[2], value[1], value[0])
        if value3 not in states_achieved:
            stack1.append(value3)
            states_achieved.add(value3)

    count += 1

    if res in states_achieved:
        print(count)
        exit(0)
