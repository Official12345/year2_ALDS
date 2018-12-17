import random

class sepChainHash:
    def __init__(self, initialTableSize = 8):
        self.table = list()
        self.tableSize = initialTableSize
        self.amountOfElements = 0
        for i in range(self.tableSize):
            self.table.append(set())
            
    def __repr__(self):
        return str(self.table)

    def makeIndex(self, element):
        return hash(element) % self.tableSize

    def almostFull(self):
        if (self.amountOfElements / self.tableSize) > 0.75:
            return True
        return False
#-----------------------------------------------------------------------------#
                                #OWN FUNCTIONS#
    def search(self, element):
        location = self.makeIndex(element)
        if element in self.table[location]:
            return True
        return False

    def insert(self, element):
        location = self.makeIndex(element)
        self.table[location].add(element)
        self.amountOfElements += 1
        if self.almostFull():
            self.rehash(self.tableSize * 2)

    def delete(self, element):
        location = self.makeIndex(element)
        if element in self.table[location]:
            self.table[location].remove(element)

    def rehash(self, newLen):
        oldElements = list()
        for subList in self.table:
            for element in subList:
                oldElements.append(element)
        self.table.clear()
        self.tableSize = newLen
        for i in range(self.tableSize):
            self.table.append(set())
        for element in oldElements:
            self.insert(element)
        print("Table has been rehashed\nNew Table:\n", str(self.table))

myHash = sepChainHash()
randomList = []
for i in range (200):
    randomList.append(random.random()*random.randint(0, 100))
for element in randomList:
    myHash.insert(element)
for i in range(100):
    myHash.delete(i)
print("\nChainList after deletion:\n", myHash, "\n")
print("Expecting True:", myHash.search(randomList[-1]))
print("Expecting False:", myHash.search(10))