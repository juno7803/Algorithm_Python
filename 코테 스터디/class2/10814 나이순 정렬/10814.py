from sys import stdin
input = stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
    arr[i].append(i)

arr.sort(key=lambda x: (int(x[0]), x[2]))

for ele in arr:
    print(' '.join(ele[:2]))
