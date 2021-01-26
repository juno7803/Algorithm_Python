from sys import stdin
input = stdin.readline

n, long = map(int, input().split())
a = []
for i in range(n):
    tmp = int(input())
    a.append(tmp)

short = min(a)
while(True):
    num = 0
    for i in a:
        num += int(i/short)
    if(num >= long):
        print(short)
        break
    else:
        short -= 1
