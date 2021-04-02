from sys import stdin
input = stdin.readline

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(1, D):
    oven[i] = min(oven[i-1], oven[i])

ans = 0
right = D-1
for i in range(N):
    left = 0
    while left < right:
        mid = (left + right) // 2
        if oven[mid] >= pizza[i]:
            ans = mid
            left = mid+1
        else:
            right = mid
    right = ans

if(ans == 0):
    print(ans)
else:
    print(ans+1)

# 75%에서 틀리는데 이유를 모르겠음
