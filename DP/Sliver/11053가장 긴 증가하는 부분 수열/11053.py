from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[j]+1 > dp[i]:
            dp[i] += 1
    ans = max(ans, dp[i])

print(ans+1)
