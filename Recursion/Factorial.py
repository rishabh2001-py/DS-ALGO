def factorial(n):
    if n == 1 or n == 0:
        return n
    fact = factorial(n - 1)
    return fact * n


if __name__ == '__main__':
    for i in range(8):
        print(factorial(i))
