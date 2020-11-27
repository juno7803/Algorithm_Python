from sys import stdin
import heapq
input = stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if (x == 0):
        if(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[-x,x])

# https://www.daleseo.com/python-heapq/