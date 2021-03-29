from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())  # 동기의 수
m = int(input())  # 리스트의 길이
adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


def bfs(start):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = 1
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in adj[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v]+1


bfs(1)
cnt = 0
for i in visited:
    if 1 < i <= 3:
        cnt += 1
print(cnt)
# 1 2, 3
# 2 1, 3
# 3 1, 2, 4
# 4 3, 5
# 5 4

# 친구, 친구의 친구 까지 가능, 1-2-3 가능, 1-3-4 가능, 1-3-4-5 불가능(친구의 친구의 친구)
# 즉, BFS로 두칸만 찾기
