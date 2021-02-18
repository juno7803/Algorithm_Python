from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
coin = [int(input()) for _ in range(n)]  # append 대신 이렇게 사용하기
for c in coin:
    for i in range(1, k+1):
        if(i == c):  # 2원을 만들기 위해 2원짜리 동전을 써야하는 경우(2원 1개)
            dp[i] += 1
        # dp를 활용하기 위함 -> dp[구해야 하는 값 - 코인의 가치] 는 결국 현재 코인을 더해 dp[구해야 하는 값] 과 같다.
        elif(i > c):
            dp[i] = dp[i] + dp[i-c]
print(dp[k])
