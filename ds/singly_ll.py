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

    def delete(self, val):

        if not self.head:
            return
        
        if self.head.data == val:
            self.head = self.head.next
            return
        

        curr = self.head
        prev = self.head

        while curr:
            
            if curr.data == val:
                break

            prev = curr
            curr = curr.next

        # the value didnt exist
        if not curr:
            return

        prev.next = curr.next
        
    def delete_at(self, idx):

        if not self.head:
            return

        if idx == 0:
            self.head = self.head.next
            return

        curr = self.head
        prev = self.head

        my_idx = 0

        while curr:

            if my_idx > idx:
                return -1

            if idx == my_idx:
                break

            prev = curr
            curr = curr.next
            my_idx += 1


        prev.next = curr.next
        
    def search(self, val):

        if not self.head:
            return
        
        if self.head.data == val:
            return True
        
        curr = self.head

        while curr.next:
            
            if curr.data == val:
                return True
            
            curr = curr.next
        
        return False
    
    def reverse(self):

        if not self.head:
            return
        
        prev_node = None
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next
            # previous has to become the next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node


def test_singly_linked_list():
    ll = SinglyLinkedList()

    # Append tests
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert str(ll) == "10 -> 20 -> 30"

    # Prepend test
    ll.prepend(5)
    assert str(ll) == "5 -> 10 -> 20 -> 30"

    # Insert at index 2
    ll.insert(2, 15)
    assert str(ll) == "5 -> 10 -> 15 -> 20 -> 30"

    # Insert at head (index 0)
    ll.insert(0, 1)
    assert str(ll) == "1 -> 5 -> 10 -> 15 -> 20 -> 30"

    # Insert at end (index > len should do nothing)
    ll.insert(100, 99)
    assert str(ll) == "1 -> 5 -> 10 -> 15 -> 20 -> 30"

    # Search test
    assert ll.search(15) == True
    assert ll.search(99) == False

    # Delete by value
    ll.delete(15)
    assert str(ll) == "1 -> 5 -> 10 -> 20 -> 30"

    ll.delete(1)  # delete head
    assert str(ll) == "5 -> 10 -> 20 -> 30"

    ll.delete(30)  # delete tail
    assert str(ll) == "5 -> 10 -> 20"

    ll.delete(99)  # delete non-existent
    assert str(ll) == "5 -> 10 -> 20"

    # Delete at index
    ll.delete_at(1)
    assert str(ll) == "5 -> 20"

    ll.delete_at(0)
    assert str(ll) == "20"

    ll.delete_at(0)
    assert str(ll) == ""

    ll.delete_at(0)  # empty list
    assert str(ll) == ""

    # Append again and reverse
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "1 -> 2 -> 3"
    ll.reverse()
    assert str(ll) == "3 -> 2 -> 1"

    print("All tests passed!")

test_singly_linked_list()