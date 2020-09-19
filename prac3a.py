class ArrayQ:
    default_capacity = 10
    def __init__(self):
        self.data = [None] * ArrayQ.default_capacity

    def isEmpty(self):
        return self.size == 0

    def enqueueFront(self, data):
        self.data.append(data)
        
    def dequeueBack(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

dq=ArrayQ()

print(dq.enqueueFront('Shraddha'))
print(dq.size())
print(dq.size())
