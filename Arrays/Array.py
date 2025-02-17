class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.core = [None] * self.capacity

    def add(self, e):
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
        self.core[self.size] = e
        self.size += 1

    def delete_ByIndex(self, index):
        if index >= self.size or index < -self.size:
            print("Cannot delete, The index is out of range!")
            return
        if index < 0:
            index += self.size  # Convert negative index to positive

        for i in range(index, self.size - 1):
            self.core[i] = self.core[i + 1]

        self.size -= 1
        self.core[self.size] = None  # Remove reference to last element

        if self.size < self.capacity // 4 and self.capacity > 4:
            self._resize(max(4, self.capacity // 2))

    def get(self, index):
        if index >= self.size or index < -self.size:
            print("Cannot get the element, The index is out of range!")
            return None
        return self.core[index if index >= 0 else self.size + index]

    def set(self, index, val):
        if index >= self.size or index < -self.size:
            print("The index is not valid")
            return
        self.core[index if index >= 0 else self.size + index] = val

    def _resize(self, new_capacity):
        new_core = [None] * new_capacity
        for i in range(self.size):
            new_core[i] = self.core[i]
        self.core = new_core
        self.capacity = new_capacity


# Test the fixed implementation
arr = Array(4)

arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
arr.add(5)  # Triggers resizing

