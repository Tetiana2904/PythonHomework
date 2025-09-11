def sum_even_indexes(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for i in range(0, len(lst), 2):
        total += lst[i]
    return total * lst[-1]









