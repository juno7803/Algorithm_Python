from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(M)]
# 가중치를 기준으로 정렬
adj = sorted(adj, key=lambda a: a[2])
parent = [i for i in range(N+1)]


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y


def kruskal():
    ans = 0
    for a in adj:
        x, y, cost = a
        if find(x) == find(y):
            continue
        else:
            ans += cost
            union(x, y)
    print(ans)


kruskal()
