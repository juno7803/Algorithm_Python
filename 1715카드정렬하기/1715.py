from sys import stdin
import heapq
input = stdin.readline

n = int(input())
heap = []
result = 0

for _ in range(n):
    ele = int(input())
    heapq.heappush(heap,ele)

for _ in range(n-1):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    result += x+y
    heapq.heappush(heap,x+y)

print(result)