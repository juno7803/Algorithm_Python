from sys import stdin
input = stdin.readline

word = list(input().strip())
left = []
right = []
n = int(input())

for i in range(len(word)):
    left.append(word[i])

for i in range(n):
    cmd = input().split()
    if(cmd[0] == 'L'):
        if(len(left) != 0):
            tmp = left.pop()
            right.append(tmp)
    elif(cmd[0] == 'D'):
        if(len(right) != 0):
            tmp = right.pop()
            left.append(tmp)
    elif(cmd[0] == 'B'):
        if(len(left) != 0):
            left.pop()
    elif(cmd[0] == 'P'):
        left.append(cmd[1])
right.reverse()
print("".join(left+right))
