def getNumbers(s):
    numberlist = []
    last = False
    for i in s:
        if i.isdigit():
            if last:
                numberlist[len(numberlist) - 1] *= 10
                numberlist[len(numberlist) - 1] += int(i)
            else:
                numberlist.append(int(i))
            last = True
        else:
            last = False
    return numberlist

mystring = "wdubwdo1213nj455k768kn3l46n5l4"
print(getNumbers(mystring))
