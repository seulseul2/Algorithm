from re import X


def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return 1

n = int(input())
print(factorial(n))