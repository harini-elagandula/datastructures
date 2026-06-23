class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new

    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end=" -> " if itr.next else "")
            itr = itr.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

ll = LinkedList()
for value in [10, 20, 30, 40, 50]:
    ll.add_end(value)

print("Original list:")
ll.display()
ll.reverse()
print("Reversed list:")
ll.display()
        