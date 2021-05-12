from sys import stdin
input = stdin.readline

n = int(input())
sol = list(map(int, input().split()))

m = int(input())
ans = list(map(int, input().split()))

dicts = {}

for s in sol:
    if(s in dicts):
        dicts[s] += 1
    else:
        dicts[s] = 1

result = []
for a in ans:
    if(a in dicts):
        result.append(dicts[a])
    else:
        result.append(0)

print(*result)
