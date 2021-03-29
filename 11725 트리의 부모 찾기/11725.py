from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]  # zero padding
visited = [False] * (n+1)
ans = [0 for _ in range(n+1)]

for _ in range(n-1):  # 인접 리스트 할당
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in adj[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                ans[i] = v


bfs(1)
for i in range(2, n+1):
    print(ans[i])
