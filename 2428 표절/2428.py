from sys import stdin
input = stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
ans = 0

for i in range(n):
    l = i
    r = n
    while l < r:
        mid = (l+r) // 2
        if arr[i] >= arr[mid]*0.9:
            l = mid+1
        else:
            r = mid
    ans += r-i-1  # 총 r번 비교, i는 자기 자신이므로 횟수 제외(i부터 r까지)
print(ans)
