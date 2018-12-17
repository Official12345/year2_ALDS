def check(a, i): #check if a can be added to ListOfQueens
    n = len(a)
    return not (i in a or i+n in [a[j]+j for j in range(n)] or i-n in [a[j]-j for j in range(n)])

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X", end= " ")
            else:
                print("*", end= " ")
        print()
    print()

def rsearch(amountOfQueens, ListOfQueens):
    global solutions
    for i in range(amountOfQueens):
        if check(ListOfQueens, i):
            ListOfQueens.append(i)
            if len(ListOfQueens) == amountOfQueens:
                solutions.append(list(ListOfQueens))
                rsearch(amountOfQueens, ListOfQueens)
            else:
                if rsearch(amountOfQueens, ListOfQueens):
                    return True
            ListOfQueens.pop(-1)
    return False

QueensList = []
solutions = []
t = 0
rsearch(8, QueensList)
print(solutions)

print("Amount of solutions:", len(solutions))
printQueens(solutions[0])