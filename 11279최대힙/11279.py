from sys import stdin
import heapq
input = stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if (x == 0):
        if(len(heap)!= 0):
            val = heapq.heappop(heap)
            print(val)
        else:
            print(0)
    else:
        heapq.heappush(heap,x)

