class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None

    def __str__(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return " -> ".join(result)
    
    def append(self, val):

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def prepend(self, val):

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
    

        new_node.next = self.head
        self.head = new_node

    def insert(self, idx, val):

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
        
        if idx == 0:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            return

        curr_idx = 0
        curr = self.head
        prev = self.head

        while curr:

            if idx == curr_idx:
                prev.next = new_node
                new_node.next = curr
                break
            
            prev = curr
            curr = curr.next
            curr_idx += 1


ll = SinglyLinkedList()
ll.append(3)
ll.append(5)
ll.prepend(1)
ll.append(7)
ll.insert(2, 15)

print(ll)