num1 = float(input("Wpisz pierwszą liczbę: "))
op = input("Wpisz operator (+, -, *, /): ")
num2 = float(input("Wpisz drugą liczbę: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/" and num2 != 0:
    print(num1 / num2)
else:
    print("Błąd")
