from sys import stdin
input = stdin.readline

n = int(input())
w = [int(input())for _ in range(n)]  # wine
# same as
# w = []
# for i in range(n):
#   w.append(int(input()))
dp = [0 for _ in range(n+1)]
dp[1] = w[0]
if(n >= 2):
    dp[2] = w[0] + w[1]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + w[i-1], dp[i-3] + w[i-2] + w[i-1])

print(dp[n])
