from sys import stdin
input = stdin.readline

n = int(input())
chu = list(map(int, input().split()))
chu.sort() # 입력받은 추 무게 오름차순 정렬

weight = 1 # 정수이므로 1을 더하면 최소값을 만들 수 있으므로
for i in range(n):
    if weight < chu[i]: # 새로 들어올 추의 무게보다 여태까지의 합이 작으면 끝
        break 
    weight += chu[i]

print(weight)