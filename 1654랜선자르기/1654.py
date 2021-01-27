from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
left, right = 1, max(a)
while(left <= right):
    cnt = 0
    mid = (left + right) // 2
    for i in a:
        cnt += i // mid
    if(cnt >= m):
        left = mid+1
        ans = mid
    elif(cnt < m):
        right = mid-1
print(ans)
# while(True)로 풀었을 때, 시간초과 뜨는 이유는 뭘까..?
