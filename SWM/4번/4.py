# from sys import stdin
# input = stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# cnt = 0

# for i in range(3):
#     visited = [0 for _ in range(n)]
#     start = i
#     cur = 0
#     while(True):
#         if(visited[start] == 1):
#             break
#         else:
#             visited[start] = 1
#             start += arr[start]
#     for j in range(n):
#         if (visited[j] == 1):
#             cur += 1
#     cnt = max(cnt, cur)

# print(cnt+1)

from sys import stdin
input = stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(3):
        visited = [0 for _ in range(n)]
        start = i
        cur = 0
        while(True):
            if(visited[start] == 1):
                break
            else:
                visited[start] = 1
                start += arr[start]
        for j in range(n):
            if (visited[j] == 1):
                cur += 1
        cnt = max(cnt, cur)

    print(cnt+1)


if __name__ == "__main__":
    main()
