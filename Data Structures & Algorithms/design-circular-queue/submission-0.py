class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k # capacity
        self.queue = [None] * k
        self.front = 0 # index of the current front item
        self.rear = 0 # location where the next item will be inserted
        self.size = 0 # number of items currently stored

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.queue[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else: 
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()