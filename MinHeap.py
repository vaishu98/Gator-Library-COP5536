class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        # Using a tuple with the first element as negative infinity for comparison
        self.Heap[0] = (float('-inf'),)
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos][0] > self.Heap[self.leftChild(pos)][0]) or (self.Heap[pos][0] > self.Heap[self.rightChild(pos)][0]):
                if self.Heap[self.leftChild(pos)][0] < self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                elif (self.Heap[self.leftChild(pos)][0] == self.Heap[self.rightChild(pos)][0]) and (self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]):
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current][0] < self.Heap[self.parent(current)][0]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

        while (current > 1) and (self.Heap[current][0] == self.Heap[self.parent(current)][0]) and (self.Heap[current][2] < self.Heap[self.parent(current)][2]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def getValues(self):
        return self.Heap[1:self.size + 1]

    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped



'''
print('The minHeap is ')
minHeap = MinHeap(15)
print(minHeap.getValues())
minHeap.insert((5, 1, "A"))
minHeap.insert((3,1, "B"))
print("The Min val is " + str(minHeap.remove()))
print("The Min val is " + str(minHeap.remove()))
print(minHeap.getValues())

minHeap.insert((17,1, "C"))
minHeap.insert((16,1, "O"))
minHeap.insert((2,1, "P"))
minHeap.insert((11,1, "Q"))
minHeap.insert((2,1, 'A'))
print(minHeap.getValues())
print("The Min val is " + str(minHeap.remove()))
print(minHeap.getValues())
print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))
print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))

print("The Min val is " + str(minHeap.remove()))
print('The minHeap is ')
minHeap = MinHeap(15)
minHeap.insert((5, 1, "A"))
minHeap.insert((3, 1, "B"))
minHeap.insert((17, 1, "C"))
minHeap.insert((16, 1, "O"))
minHeap.insert((2, 1, "P"))
minHeap.insert((11, 1, "Q"))
minHeap.insert((2, 1, 'A'))
print(minHeap.getValues())
print("The Min val is " + str(minHeap.remove()))
print(minHeap.getValues())
print("The Min val is " + str(minHeap.remove()))
'''
