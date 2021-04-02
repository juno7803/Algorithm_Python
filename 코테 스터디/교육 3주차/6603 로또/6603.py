from itertools import combinations
from sys import stdin
input = stdin.readline

while(True):
    arr = list(map(int, input().split()))
    newArr = []
    if(arr[0] == 0):
        break
    else:
        for i in list(combinations(arr[1:], 6)):
            newArr.append(i)
        for a in sorted(newArr):
            print(*a)
        print()


# a = []
# items = [1, 2, 3, 4]

# for i in list(combinations(items, 2)):
#     a.append(i)
