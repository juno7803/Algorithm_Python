N, M = map(int,input().split())
a = set()
b = set()

for _ in range (N):
    a.add(input())
for _ in range (M):
    b.add(input())

ans = sorted(a&b)
print(len(ans))
for i in ans:
    print(i)
