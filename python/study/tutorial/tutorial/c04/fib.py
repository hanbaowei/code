
def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return b


if __name__ == '__main__':
    r = fib(10)
    print r