import sys

N = int(sys.stdin.readline())
a = set(map(int,input().split()))
M = int(sys.stdin.readline())
b = list(map(int,input().split()))

for i in b:
    if i in a:
        print(1)
    else:
        print(0)