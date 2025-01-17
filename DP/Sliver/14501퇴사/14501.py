from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    if arr[i][0] + i > n:
        dp[i] = dp[i+1]  # 만약 해당일자를 더했을 때 초과한 경우
    else:
        dp[i] = max(arr[i][1] + dp[i+arr[i][0]], dp[i+1])

print(dp[0])
