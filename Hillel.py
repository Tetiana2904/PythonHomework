while True:
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))
    op = input("Дія (+, -, *, /): ")
 
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("На нуль не можна")
        else:
            print(a / b)

    again = input("Продовжити? (yes/y): ")
    if again.lower() not in ["yes", "y"]:
        break









