def move_zeros(lst):
    new_list = []
    count_zeros = 0
    for i in lst:
        if i == 0:
            count_zeros += 1
        else:
            new_list.append(i)
    for i in range(count_zeros):
        new_list.append(0)
    return new_list










