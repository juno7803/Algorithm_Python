from sys import stdin
input = stdin.readline

n = int(input())
atm = list(map(int,input().split()))

atm.sort()
eleSum = 0
tmp = list()
for i in atm:
    eleSum += i
    tmp.append(eleSum)
print(sum(tmp))