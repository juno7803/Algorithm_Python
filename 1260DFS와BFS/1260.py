from sys import stdin
from collections import deque

n,m,v = map(int,stdin.readline().split())
adj = [list() for _ in range(n+1)]
check = [0 for _ in range(n+1)]
dfsVisited = []
bfsVisited = []
q = deque()

# 인접리스트 초기화
for i in range(m):
    a,b = map(int,stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

# 인접리스트 adj 오름차순 정렬(문제 조건)
for ele in adj:
    ele.sort()

def dfs(x):
    check[x] = 1
    dfsVisited.append(x)
    for i in range(len(adj[x])):
        y = adj[x][i]
        if(check[y] == 0):
            dfs(y)

def bfs(v):
    check[v] = 1
    q.append(v)
    bfsVisited.append(v)
    while(len(q)!=0):
        x = q.popleft()
        for i in range(len(adj[x])):
            y = adj[x][i]
            if(check[y] == 0):
                check[y] = 1
                q.append(y)
                bfsVisited.append(y)

dfs(v)
# dfs에 사용한 check 재사용 위해 0으로 다시 초기화
check = [0 for _ in range(n+1)]
bfs(v)
print(" ".join(map(str,dfsVisited)))
print(" ".join(map(str,bfsVisited)))
