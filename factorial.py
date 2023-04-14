# factorial.py

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Введите число для нахождения факториала: "))

print("Факториал", number, "равен", factorial(number))
