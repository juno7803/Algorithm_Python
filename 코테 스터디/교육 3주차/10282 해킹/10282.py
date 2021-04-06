from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

INF = int(1e9)


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heappop(heap)
        if distance[now] > dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if distance[next_node] > cost:
                distance[next_node] = cost
                heappush(heap, (cost, next_node))


test_case = int(input())
for _ in range(test_case):
    n, d, c = map(int, input().split())  # n : 노드 수, d : 간선 수, c : 시작점
    distance = [INF for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    result = []
    for _ in range(d):  # d: 간선 갯수
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c)

    num = 0
    time = 0
    for d in distance:
        if d < INF:
            num += 1
            time = max(time, d)
    print(num, time)
