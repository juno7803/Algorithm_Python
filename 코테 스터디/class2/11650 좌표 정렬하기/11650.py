from sys import stdin
stdin.readline

n = int(input())
location = [list(map(int, input().split())) for _ in range(n)]

location.sort(key=lambda x: (x[0], x[1]))

for l in location:
    print(' '.join(map(str, l)))
