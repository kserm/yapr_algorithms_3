def parenthesis_generator(n, i=0, j=0, res=''):
    if i + j == 2*n:
        print(res)
    else:
        if i < n:
            parenthesis_generator(n, i + 1, j, res + '(')
        if i > j:
            parenthesis_generator(n, i, j + 1, res + ')')


if __name__ == '__main__':
    n = int(input())
    parenthesis_generator(n)
