from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
maze = [[0]*m for _ in range(n)]
for i in range(n):
    tmp = stdin.readline()
    for j in range(m):
        maze[i][j] = int(tmp[j])

visited = [[0]*m for _ in range(n)]
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q.append((0, 0))
visited[0][0] = 1

while len(q) != 0:
    x, y = q.popleft()
    for i in range(4):  # 상 하 좌 우
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < n and 0 <= ny < m):
            if(visited[nx][ny] == 0 and maze[nx][ny] == 1):  # 방문한 적이 없고, 칸이 있다면,
                q.append((nx, ny)) # bfs의 큐에 추가해주고,
                visited[nx][ny] = visited[x][y] + 1 # 방문한 곳에 값을 넣어준다!

print(visited[n-1][m-1])
