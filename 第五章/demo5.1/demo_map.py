def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    fac = factorial
    fac_list = list(map(fac, range(11)))
    print(fac_list)
