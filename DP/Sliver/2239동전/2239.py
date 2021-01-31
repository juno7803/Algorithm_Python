from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coin = []
dp = [0 for _ in range(k+1)]
for i in range(n):
    coin.append(int(input()))
dp[1] = 1
for j in coin:
    for i in range(1, k+1):
        # if(i > j):
        dp[i] = dp[i] + dp[i-j]
print(dp[n])
