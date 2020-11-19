from sys import stdin
input = stdin.readline

n = int(input())
ele = []

for i in range(n):
    a,b = map(int,input().split())
    ele.append([a,b])
ele = sorted(ele, key=lambda x: x[0]) # a(첫 번째 원소로 정렬)
ele = sorted(ele, key=lambda x: x[1]) # b(두 번째 원소로 정렬)
# ele.sort(key=lambda x: (x[1],x[0])) # 와 같이 한번에 정렬 가능

end = 0
cnt = 0
for i in ele:
    if i[0] >= end:
        cnt += 1
        end = i[1]

# for i,j in ele:
#     if i >= end:
#         cnt += 1
#         end = j
print(cnt)