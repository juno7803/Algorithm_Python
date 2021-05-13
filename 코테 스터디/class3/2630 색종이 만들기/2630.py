from sys import stdin
input = stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0


def sol(x, y, n):
    global white, blue
    color = paper[x][y]  # 시작점
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                # 아래 조건들로 n의 범위를 좁혀가다가, if color != paper[i][j] 조건을 모두 통과하게 되면 아래의 color white or blue를 + 시켜준다.
                sol(x, y, n//2)
                sol(x, y + n//2, n//2)
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


sol(0, 0, n)
print(white)
print(blue)
