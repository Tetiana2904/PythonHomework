






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




