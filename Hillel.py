num = int(input("5-значне число: "))
a = num // 10000
b = (num % 10000) // 1000
c = (num % 1000) // 100
d = (num % 100) // 10
e = num % 10
reversed_num = e*10000 + d*1000 + c*100 + b*10 + a
print(reversed_num)