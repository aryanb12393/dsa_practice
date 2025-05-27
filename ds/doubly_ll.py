class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

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
            self.tail = new_node
            return
        
        #prev_node = None

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    
    def prepend(self, val):
        
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert(self, idx, val):

        new_node = Node(val)

        if idx == 0:
            self.prepend(val)
            return

        curr_idx = 0
        curr = self.head

        while curr and curr_idx < idx:
            # print(curr.data)
            curr = curr.next
            curr_idx += 1
           
        
        # it was bigger, this is invalid
        if curr is None and curr_idx == idx:
            self.append(val)
            return

        if curr is None:
            return

        # previous node's next = the new node
        # current node's prev = the new node

        # new nodes next = current node
        # new nodes prev = the prev node

        prev_node = curr.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = curr
        curr.prev = new_node
    
    def delete(self, idx):

        if not self.head:
            return
        
        if idx == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        curr = self.head
        curr_idx = 0

        while curr and curr_idx < idx:

            curr = curr.next
            curr_idx += 1

        
        if curr is None:
            return
        
        if curr.next:
            curr.next.prev = curr.prev
            
        else:
            self.tail = curr.prev  # deleting tail

        if curr.prev:
            curr.prev.next = curr.next
        

        



ll = DoublyLinkedList()
ll.append(5)
ll.append(3)
ll.append(2)
ll.insert(0, 1)

ll.insert(4,4)
ll.delete(0)
# ll.delete(0)
# ll.delete(0)
print(ll)


    