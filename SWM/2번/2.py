# from sys import stdin
# input = stdin.readline

# p, n, h = map(int, input().split())
# arr = []
# for i in range(p):
#     arr.append([i+1, h, 0])

# for _ in range(n):
#     com, use_hour = map(int, input().split())
#     if(arr[com-1][1] < use_hour):
#         pass
#     else:
#         arr[com-1][1] - use_hour
#         arr[com-1][2] += use_hour*1000

# for i in range(p):
#     print(f"{arr[i][0]} {arr[i][2]}")

from sys import stdin
input = stdin.readline


def main():
    p, n, h = map(int, input().split())
    arr = []
    for i in range(p):
        arr.append([i+1, h, 0])

    for _ in range(n):
        com, use_hour = map(int, input().split())
        if(arr[com-1][1] < use_hour):
            pass
        else:
            arr[com-1][1] - use_hour
            arr[com-1][2] += use_hour*1000

    for i in range(p):
        print(f"{arr[i][0]} {arr[i][2]}")


if __name__ == "__main__":
    main()
