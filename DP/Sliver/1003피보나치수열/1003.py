from sys import stdin
input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(max(arr)+1)]
for i in arr:
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for j in range(2, i+1):
        dp[j] = [dp[j-1][0] + dp[j-2][0], dp[j-1][1] + dp[j-2][1]]

for k in arr:
    print(dp[k][0], dp[k][1])
