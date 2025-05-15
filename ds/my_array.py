class Array:
    
    def __init__(self):
        self.array_capacity = 10
        self.array_size = 0
        self.array = self._make_array(self.array_capacity)

    def _make_array(self, new_capacity):
        return [None] * new_capacity
    
    def append(self, val):

        if self.array_size == self.array_capacity:
            self.resize()

        self.array[self.array_size] = val
        self.array_size += 1

    def resize(self):
        
        self.array_capacity *= 2
        new_array = self._make_array(self.array_capacity)
        
        for i in range(self.array_size):
            new_array[i] = self.array[i]

        self.array = new_array

    def size(self):
        return self.array_size
    
    def capacity(self):
        return self.array_capacity

    def pop(self):
        val = self.array[self.array_size - 1]
        self.array[self.array_size-1] = None
        self.array_size -= 1
        return val

    def get(self, index):
        return self.array[index]
    
    def insert(self, index, val):

        if self.array_size == self.array_capacity:
            self.resize()

        for i in range(self.array_size, index, -1):
            self.array[i] = self.array[i-1]
        
        self.array[index] = val
        self.array_size += 1
    
    def delete(self, index):
        
        for i in range(index, self.array_size-1):
            self.array[i] = self.array[i+1]
        
        self.array[self.array_size-1] = None
        self.array_size -= 1
    
    def find(self, val):

        for index, elt in enumerate(self.array):
            if elt == val:
                return index

        return -1
    
    def contains(self, val):

        for elt in self.array:
            if elt == val:
                return True

        return False
    
    def clear(self):

        for i in range(self.array_size):
            self.array[i] = None
        

# tests

arr = Array()

arr.append(10)
arr.append(20)
arr.append(30)
assert arr.size() == 3
assert arr.get(0) == 10
assert arr.get(1) == 20
assert arr.get(2) == 30

val = arr.pop()
assert val == 30
assert arr.size() == 2
assert arr.get(1) == 20

arr = Array()
for i in range(15):
    arr.append(i)

assert arr.size() == 15
assert arr.capacity() >= 15

for i in range(15):
    assert arr.get(i) == i

for _ in range(15):
    arr.pop()

assert arr.size() == 0

arr = Array()
for i in range(100):
    arr.append(i * 2)

assert arr.size() == 100
assert arr.capacity() >= 100
assert arr.get(50) == 100
assert arr.get(99) == 198