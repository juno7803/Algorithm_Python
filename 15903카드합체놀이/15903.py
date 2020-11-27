from sys import stdin
import heapq
# 보통의 리스트를 힙처럼 다룰 수 있도록 도와주는 모듈 (deque 등과 다르다.)
input = stdin.readline

n,m = map(int,(input().split()))
arr = list(map(int,input().split()))
heap = []

for i in arr:
    heapq.heappush(heap,i)

for _ in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap,x+y)
    heapq.heappush(heap,x+y)

print(sum(heap))
# for i in range(0,m):
#     arr.sort()
#     val = arr[i] + arr[i+1]
#     arr[i] = val
#     arr[i+1] = val

# print(sum(arr))
