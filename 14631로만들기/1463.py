n = int(input())

dp = [0 for _ in range(n+1)]

def func():
    dp[1] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            tmp = dp[i//2] + 1
            dp[i] = min(dp[i],tmp)
        if i % 3 == 0:
            tmp = dp[i//3] + 1
            dp[i] = min(dp[i], tmp)
    print(dp[n])

func()
# 파이썬에만 있는 이상한 친구..
# // 