from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = num[0]  # 초기값 설정
ans = num[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+num[i], num[i])
    ans = max(ans, dp[i])

print(ans)
