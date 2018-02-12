from heapq import *
from random import shuffle

data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)

print heap
heappush(heap,0.4)
print heap
# print heappop(heap)
print heap.pop()