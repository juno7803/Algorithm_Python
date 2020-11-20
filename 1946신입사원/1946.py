from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    p = []
    for _ in range(m):
        paper, interview = map(int,input().split())
        p.append([paper,interview])
    p = sorted(p, key=lambda a: a[0]) # 첫 번째 원소로 정렬
    cnt = 1
    min = p[0][1]
    for i in range(1,m):
        if(p[i][1] < min):
            cnt += 1
            min = p[i][1]

    print(cnt)