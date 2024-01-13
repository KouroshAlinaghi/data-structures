class MinHeap:
    def __init__(self):
        self.data = []

    def bubble_up(self, index):
        if index == 0:
            return
        parent = (index + 1) // 2 - 1
        if self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.bubble_up(parent)

    def bubble_down(self, index):
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2

        if len(self.data) - 1 < l:
            return

        if len(self.data) - 1 == l:
            if self.data[l] < self.data[index]:
                self.data[index], self.data[l] = self.data[l], self.data[index]
            return

        if self.data[index] > min(self.data[l], self.data[r]):
            index_to_be_swapped = l if self.data[l] < self.data[r] else r
            self.data[index], self.data[index_to_be_swapped] = self.data[index_to_be_swapped], self.data[index]
            self.bubble_down(index_to_be_swapped)

    def push(self, value):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def pop(self):
        self.data[-1], self.data[0] = self.data[0], self.data[-1]
        self.data.pop()
        if len(self.data) > 0:
            self.bubble_down(0)

n, d = [int(x) for x in input().split()]
times = [0] * n
heap = MinHeap()
cost = 0

a = [[0, 0, 0]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
    cost += a[i][1] * a[i][2]
a.sort()

ptr = 0

for day in range(1, d + 1):
    while ptr < n and a[ptr][0] <= day:
        heap.push([-a[ptr][2], ptr])
        ptr += 1

    if len(heap.data):
        teacher = heap.data[0][1]
        times[teacher] += 1
        cost -= a[teacher][2]

        if times[teacher] == a[teacher][1]:
            heap.pop()

print(cost)
