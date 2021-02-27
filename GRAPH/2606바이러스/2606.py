from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
visited = [False] * n  # 방문 기록을 위한 list
adj = [[] for _ in range(n+1)]
cnt = 0


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

dfs(adj, 1, visited)  # 호출

for i in range(n):
    if visited[i] == True:
        cnt += 1

print(cnt - 1)  # 1 자기자신 제외
