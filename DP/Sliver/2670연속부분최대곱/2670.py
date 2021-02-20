from sys import stdin
input = stdin.readline

n = int(input())
numbers = [float(input()) for _ in range(n)]
ans = numbers[0]  # 초기값

for i in range(1, n):
    if numbers[i] < numbers[i]*numbers[i-1]:
        numbers[i] = numbers[i]*numbers[i-1]
    ans = max(ans, numbers[i])
print("{:.3f}".format(ans))
