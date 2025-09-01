num = int(input("4-значне число: "))

a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10

print(a)
print(b)
print(c)
print(d)