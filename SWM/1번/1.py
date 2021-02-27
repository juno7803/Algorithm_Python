from sys import stdin
input = stdin.readline

arr = list(input().split())
n = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * len(arr)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for _ in range(n):
    x, y = input().split()
    adj[x].append(y)
    adj[y].append(x)

dfs(adj, 1, visited)
