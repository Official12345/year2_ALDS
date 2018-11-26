def machtv3(a, n):
    assert n > 0
    counter = 0
    m = 1
    while n > 0:
        if n%2 == 0:
            a = a * a
            n /= 2
            counter += 1
        else:
            m = m * a
            n -= 1
            counter += 1
    return m, counter

print(machtv3(3, 8))

print(3**8)