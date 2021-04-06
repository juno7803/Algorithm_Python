from sys import stdin
input = stdin.readline

INF = int(1e9)
n, m, r = map(int, input().split())
item = list(map(int, input().split()))  # 정답 계산시 쓸 아이템 담은 리스트
d = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(r):
    x, y, c = map(int, input().split())
    d[x-1][y-1] = c
    d[y-1][x-1] = c

# 가능한 모든 경로의 최소거리를 만들어 준다.


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


# 간선의 가중치 초기화 -> 자기자신은 0, 연결되지 않은 경우는 INF
floyd()
for i in range(n):
    d[i][i] = 0

ans = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if d[i][j] <= m:  # 수색 범위를 넘으면 더하지 않음
            tmp += item[j]
    ans = max(ans, tmp)

print(ans)
