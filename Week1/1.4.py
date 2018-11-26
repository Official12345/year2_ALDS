import random

counter = 0

for i in range(0, 100):
    random_list = []
    for j in range(0, 23):
        random_list.append(random.randrange(1, 366))
    random_list.sort()
    for k in range(0, 23):
        if k < 22:
            if random_list[k] == random_list[k+1]:
                counter += 1
                break

print(counter)
