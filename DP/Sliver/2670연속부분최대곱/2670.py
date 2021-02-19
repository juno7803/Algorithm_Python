# from sys import stdin
# input = stdin.readline

# n = int(input())
# nums = [float(input()) for _ in range(n)]
# dp = [0 for _ in range(n)]
# dp[0] = nums[0]
# ans = -1

# for i in range(1, n):
#     if dp[i-1] * nums[i] < nums[i]:
#         dp[i] = nums[i]
#     else:
#         dp[i] = dp[i-1] * nums[i]

# for j in range(n):
#     ans = max(ans, dp[j])
# print(round(ans, 3))
from sys import stdin
input = stdin.readline

n = int(input())
numbers = [float(input()) for _ in range(n)]
ans = -1  # 초기값

for i in range(1, n):
    if numbers[i] < numbers[i]*numbers[i-1]:
        numbers[i] = numbers[i]*numbers[i-1]
    ans = max(ans, numbers[i])
print(round(ans, 3))
