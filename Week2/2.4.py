def mybin(n):
    assert n >= 0
    if n == 1:
        return "1"
    elif n % 2 == 0:
        return mybin(n/2) + "0"
    else:
        return mybin((n - 1) / 2) + "1"

print(mybin(21))