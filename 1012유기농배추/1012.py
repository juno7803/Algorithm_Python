from collections import deque
from sys import stdin

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if(0 <= nx < n and 0 <= ny < m):
                if (check[nx][ny] == 0 and a[nx][ny] == 1):
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

n = int(stdin.readline())

for _ in range(n):
    cnt = 0
    n, m, c = map(int, stdin.readline().split())
    a = [[0] * m for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    
    for _ in range(c):
        i, j = map(int, stdin.readline().split())
        a[i][j] = 1

    # bfs
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and check[i][j] == 0:
                cnt += 1
                bfs(i, j)
    print(cnt)