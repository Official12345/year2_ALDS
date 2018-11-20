def mymax(a):
    assert len(a) > 0
    b = a[0]
    for i in a:
        assert type(i) == int or type(i) == float
        if i > b:
            b = i
    return(b)


try:
    mylist = [1, 2, 12, 3, 5, 7]
    print(mymax(mylist))
except:
    print("error test 1")

try:
    mylist2 = []
    print(mymax(mylist2))
except:
    print("error test 2")

try:
    mylist3 = ['a', 6, "3"]
    print(mymax(mylist3))
except:
    print("error test 3")