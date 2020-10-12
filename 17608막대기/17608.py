import sys
stack = []
n = int(sys.stdin.readline())
for _ in range (n):
    ele = int(sys.stdin.readline())
    stack.append(ele)

num = 1
top = stack.pop()

while len(stack)!=0:
    tmp = stack.pop()
    if(tmp > top):
        num += 1
        top = tmp
    else:
        pass
print(num)