class MinStack:

    def __init__(self):
        self.storage = []
        self.tracker = [] # only holds the mins at the points where they change

    def push(self, val: int) -> None:
        self.storage.append(val)
        
        # only record val if it's a new min (or ties with the curr min)
        if not self.tracker or val <= self.tracker[-1]:
            self.tracker.append(val)
        
    def pop(self) -> None:
        val = self.storage.pop()

        # if value removed was curr min, drop it from tracker
        if val == self.tracker[-1]:
            self.tracker.pop()

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return self.tracker[-1]
