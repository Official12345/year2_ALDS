def B(n,k):
    if(n < k):
        return False
    factorials = [[1]]
    for i in range(1, n+1):
        to_append = [1]
        for j in range(1, (min(len(factorials[i-1]), k) + 1)):
            if(j+1 > len(factorials[i-1])):
                to_append.append(factorials[i-1][j-1])
            else:
                to_append.append(factorials[i - 1][j - 1] + factorials[i - 1][j])
        factorials.append(to_append)

    for fact in factorials:
        print(fact)
    return factorials[n][k]

print("Result:", B(6,3))
print("-----------------------------------------------")
print("Result:", B(100,50))
