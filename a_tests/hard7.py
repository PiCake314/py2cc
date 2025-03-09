


def sum(l):
    acc = 0
    for e in l:
        acc += e

    return acc


def average(l):
    return sum(l) / len(l)


l = [1, 2, 3, 4, 5]
s = sum(l)
if s != 0:
    print("Sum:", s)


print("Average:", average(l))
