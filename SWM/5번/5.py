# from sys import stdin
# input = stdin.readline

# n = int(input())
# arr = []
# cnt = 0
# for i in range(n*n):
#     tmp = list(map(int, input().split()))
#     score, dnum = tmp[0], tmp[1]
#     arr.append(tmp[2:2+dnum])  # 두더지 초 모음

#     for j in arr:
#         for k in j:
#             cnt = max(k, cnt)

# sec = [[] for _ in range(cnt+1)]

# start = 1
# for j in arr:
#     for k in j:
#         sec[k].append(start)
#     start += 1

# max_score = 0
# for i in range(1, len(sec)):
#     max_score += max(sec[i])
# print(max_score)

from sys import stdin
input = stdin.readline


def main():
    n = int(input())
    arr = []
    cnt = 0
    for i in range(n*n):
        tmp = list(map(int, input().split()))
        score, dnum = tmp[0], tmp[1]
        arr.append(tmp[2:2+dnum])  # 두더지 초 모음

        for j in arr:
            for k in j:
                cnt = max(k, cnt)

    sec = [[] for _ in range(cnt+1)]

    start = 1
    for j in arr:
        for k in j:
            sec[k].append(start)
        start += 1

    max_score = 0
    for i in range(1, len(sec)):
        max_score += max(sec[i])
    print(max_score)


if __name__ == "__main__":
    main()
