import random

n = random.randint(3, 10)   
lst = []

for i in range(n):
    lst.append(random.randint(10, 99))  

if len(lst) >= 3:
    new_lst = [lst[0], lst[2], lst[1]]
else:
    new_lst = lst









