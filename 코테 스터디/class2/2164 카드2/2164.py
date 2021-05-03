from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
q = [i+1 for i in range(n)]
queue = deque(q)


while(len(queue) != 1):
    queue.popleft()
    second = queue.popleft()
    queue.append(second)

print(queue.popleft())
