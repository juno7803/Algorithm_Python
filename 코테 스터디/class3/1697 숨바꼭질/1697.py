from collections import deque
from sys import stdin
input = stdin.readline


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])  # 여기서 count 출력
            break
        for nx in (x-1, x+1, x*2):
            # dist[nx]가 0일때 만 dist[nx] = dist[x] + 1
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX+1)
bfs()
