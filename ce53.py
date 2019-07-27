# RG
# 4.15


def calculator(num1, num2, char):
    if char == '+':
        print(num1 + num2)
    elif char == '-':
        print(num1 - num2)
    elif char == '*':
        print(num1 * num2)
    elif char == '/':
        print(num1 / num2)
    elif char == '%':
        print(num1 % num2)
    elif char == 'x' or char == 'X':
        return None
    else:
        num1 = int(input("Enter num1:\t\t"))
        num2 = int(input("Enter num2:\t\t"))
        char = input("Enter character:\t")
        calculator(num1, num2, char)


calculator(100, 2, '')
