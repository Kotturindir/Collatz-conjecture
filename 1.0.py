def preparation(x_1, x_2):
    for i in x_1:
        y_1 = i
        y_2 = i
        y_3 = i
        y = [y_1, y_2, y_3]
        x_2.append(y)


def step(initial, final):
    for j in initial:
        primordial = j[0]
        going = j[1]
        check = j[2]
        if primordial not in next_step:
            if going % (2**n) == 0:
                going = going // (2**n)
                check = check / (2**n)
                if primordial < check:
                    next_step.append(primordial)
            elif going % 2 == 1:
                going = 3*going+1
                check = 3*check+1
                while going > 10**n:
                    going = going - 10**n
                y = [primordial, going, check]
                final.append(y)
            elif going % 2 == 0:
                going = going//2
                check = check/2
                if primordial < check:
                    y = [primordial, going, check]
                    final.append(y)
                    going = going+((10**n)/2)
                    while going > 10 ** n:
                        going = going - 10 ** n
                    y = [primordial, going, check]
                    final.append(y)


next_step = []
n = 1
zero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
initial = []
preparation(zero, initial)
final = []
for i in range(1, 100):
    step(initial, final)
    initial = final
    final = []
print(len(next_step), next_step)

zero = []
for i in numbers:
    for j in next_step:
        y = j + i*(10**n)
        zero.append(y)
n = 2
next_step = []
initial = []
preparation(zero, initial)
final = []
for i in range(1, 100):
    step(initial, final)
    initial = final
    final = []
print(len(next_step), next_step)

zero = []
for i in numbers:
    for j in next_step:
        y = j + i*(10**n)
        zero.append(y)
n = 3
next_step = []
initial = []
preparation(zero, initial)
final = []
for i in range(1, 100):
    step(initial, final)
    initial = final
    final = []
print(len(next_step), next_step)

zero = []
for i in numbers:
    for j in next_step:
        y = j + i*(10**n)
        zero.append(y)
n = 4
next_step = []
initial = []
preparation(zero, initial)
final = []
for i in range(1, 100):
    step(initial, final)
    initial = final
    final = []
print(len(next_step), next_step)

zero = []
for i in numbers:
    for j in next_step:
        y = j + i*(10**n)
        zero.append(y)
n = 5
next_step = []
initial = []
preparation(zero, initial)
final = []
for i in range(1, 100):
    step(initial, final)
    initial = final
    final = []
print(len(next_step), sorted(next_step))
