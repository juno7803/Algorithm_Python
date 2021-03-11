from sys import stdin
input = stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(0, n+1, 2):
    if i == 0:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i-2] * dp[2]
        for j in range(i-4, -1, -2):
            dp[i] += dp[j]*2

print(dp[n])
