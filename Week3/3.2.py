class ListNode:
 def __init__(self, data, next_node):
    self.data = data
    self.next = next_node
 def __repr__(self):
    return str(self.data)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if not self.head: # self.head == None:
            self.head = ListNode(e,None)
            self.tail = self.head
        else:
            n = ListNode(e,None)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self, e):
        if self.head:  # self.head != None:
            if self.head.data == e:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None

            else:
                current = self.head
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current


class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        if current != None:
            s = s + str(current)
            current = self.tail.next
        while current != self.tail:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.tail: # self.tail == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e,self.tail.next)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self, e):
        if self.tail:
            current = self.tail
            if self.tail.data == e:
                if current.next == self.tail:
                    self.tail = None
                else:
                    while current.next.next != self.tail:
                        current = current.next
                    current.next.next = self.tail.next
                    self.tail = current.next
                    return
            while current.next != self.tail:
                if current.next.data == e:
                    current.next = current.next.next
                    return
                current = current.next


mylist = MyCircularLinkedList()
print(mylist)
mylist.addLast(12)
mylist.addLast(22)
mylist.addLast(32)
print(mylist)
mylist.delete(22)
print(mylist)
mylist.delete(12)
print(mylist)
mylist.delete(32)
print(mylist)