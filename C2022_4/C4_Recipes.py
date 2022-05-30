N, a, b, c = map(int, input().split())
res = tuple(map(int, input().split()))

init = (a, b, c)
states_achieved = {init}
count = 0

stack1 = [init]
stack2 = []

if res == init:
    print(count)
else:
    while True:
        for elem in stack1:
            value1 = ((elem[0] + elem[1]) % N, (elem[1] + elem[2]) % N, (elem[2] + elem[0]) % N)
            if value1 not in states_achieved:
                stack2.append(value1)
                states_achieved.add(value1)

            value2 = ((elem[0] + 1) % N, (elem[1] - 1) % N, elem[2])
            if value2 not in states_achieved:
                stack2.append(value2)
                states_achieved.add(value2)

            value3 = (elem[2], elem[1], elem[0])
            if value3 not in states_achieved:
                stack2.append(value3)
                states_achieved.add(value3)

        count += 1

        if res in states_achieved:
            print(count)
            break

        stack1.clear()

        for elem in stack2:
            value1 = ((elem[0] + elem[1]) % N, (elem[1] + elem[2]) % N, (elem[2] + elem[0]) % N)
            if value1 not in states_achieved:
                stack1.append(value1)
                states_achieved.add(value1)

            value2 = ((elem[0] + 1) % N, (elem[1] - 1) % N, elem[2])
            if value2 not in states_achieved:
                stack1.append(value2)
                states_achieved.add(value2)

            value3 = (elem[2], elem[1], elem[0])
            if value3 not in states_achieved:
                stack1.append(value3)
                states_achieved.add(value3)

        count += 1

        if res in states_achieved:
            print(count)
            break

        stack2.clear()