a = float(input("перше число: "))
b = float(input("друге число: "))
op = input("Що зробити?(+, -, *, /): ")

if op == "+":
    print("Результат =", a + b)
elif op == "-":
    print("Результат =", a - b)
elif op == "*":
    print("Результат =", a * b)
elif op == "/":
    if b == 0:
        print("Не ділиться")
    else:
        print("Результат =", a / b)



def move_last(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    new_list = [lst[-1]]
    for i in range(len(lst)-1):
        new_list.appen


def split_list(lst):
    if len(lst) == 0:
        return [[], []]
    mid = (len(lst) + 1) // 2
    first = []
    second = []
    for i in range(mid):
        first.append(lst[i])
    for i in range(mid, len(lst)):
        second.append(lst[i])
    return [first, second]


