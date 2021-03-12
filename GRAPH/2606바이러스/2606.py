from sys import stdin
input = stdin.readline


def dfs(v):
    visited[v] = 1
    for i in adj[v]:
        if not visited[i]:
            dfs(i)


n = int(input())
m = int(input())
visited = [0 for _ in range(n+1)]  # 방문 기록을 위한 list
adj = [[] for _ in range(n+1)]  # zero padding

for _ in range(m):  # 인접 리스트 할당
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


dfs(1)  # 호출
cnt = 0
for i in visited:
    if i == 1:
        cnt += 1

print(cnt-1)  # 시작점인 1 제외
