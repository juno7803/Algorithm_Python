from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
chess = [input().rstrip('\n') for _ in range(m)]
result = []

for i in range(n - 7):
    for j in range(m - 7):
        idx1 = 0  # start with W
        idx2 = 0  # start with B
        for x in range(i, i+8):
            for y in range(j, j+8):
                if(i+j) % 2 == 0:
                    if chess[x][y] != 'W':
                        idx1 += 1
                    if chess[x][y] != 'B':
                        idx2 += 1
                else:
                    if chess[x][y] != 'B':
                        idx1 += 1
                    if chess[x][y] != 'W':
                        idx2 += 1
        result.append(idx1)
        result.append(idx2)

print(result)
