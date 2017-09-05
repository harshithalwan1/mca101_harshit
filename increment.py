def increment(n):
    n = 5
    ''' objective : to add numbers using recursion
    input parameters : number to increment
    return : incremented number
    '''
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

