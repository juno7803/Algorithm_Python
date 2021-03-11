from sys import stdin
input = stdin.readline

n, s, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
visited[0][s] = 1  # 초기값 설정

for i in range(1, n+1):
    for j in range(m+1):
        if visited[i-1][j] == 0:
            continue
        if j + arr[i-1] <= m:
            visited[i][j+arr[i-1]] = 1
        if j - arr[i-1] >= 0:
            visited[i][j-arr[i-1]] = 1

ans = -1  # 연주할 수 없는 경우 : "-1"
for k in range(m, -1, -1):
    if visited[n][k] == 1:
        ans = max(ans, k)

print(ans)
