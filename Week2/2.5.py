def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random

counter = 0
#functie van joop
def qsort(a,low=0,high=-1):
    global counter
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
            counter += 1
                            # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
        swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
        if m > 0:
            qsort(a,low,m-1)
        qsort(a,m+1,high)

#modified functie van joop
def qsortmod(a,low=0,high=-1):
    global counter
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, min(a))
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
            counter += 1
                            # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
        swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
        if m > 0:
            qsortmod(a,low,m-1)
        qsortmod(a,m+1,high)

a = [0]*10000
for i in range(10000):
    a[i] = random.randint(0,10000)
qsortmod(a)
print("modified number of comparisons:", counter)
counter = 0
qsort(a)
print("normal number of comparisons:", counter)
counter = 0