def factorial(n):
    '''n! 这是我见到的最简洁的写法了'''
    return 1 if n < 2 else n * factorial(n - 1)

if __name__ == '__main__':

    m = factorial(3)
    print(m)
    print(factorial.__doc__)
    print(type(factorial))
