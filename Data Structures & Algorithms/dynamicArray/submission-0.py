class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.storage = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        self.storage[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.storage[self.size] = n
        self.size += 1
        
    def popback(self) -> int:
        popped = self.storage[self.size-1]
        self.size -= 1
        return popped

    def resize(self) -> None:
        self.capacity = self.capacity * 2

        new_storage = [0] * self.capacity

        for i in range(self.size):
            new_storage[i] = self.storage[i]

        self.storage = new_storage

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity