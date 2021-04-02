from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(n+1)]

for _ in range(m):
    op = list(map(int, input().split()))
    if(op[0] == 1):
        train[op[1]][op[2]] = 1
    elif(op[0] == 2):
        train[op[1]][op[2]] = 0
    elif(op[0] == 3):
        for i in range(19, 1, -1):
            train[op[1]][i] = train[op[1]][i-1]
        train[op[1]][0] = 0
    elif(op[0] == 4):
        for i in range(1, 20):
            train[op[1][i-1]] = train[op[1][i]]
        train[op[1]][19] = 0

print(train)
