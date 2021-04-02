from sys import stdin
input = stdin.readline


def mult_matrix(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result


def solution(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mult_matrix(n, matrix, matrix)
    else:
        tmp = solution(n, b//2, matrix)
        if b % 2 == 0:  # 짝수
            return mult_matrix(n, tmp, tmp)
        else:  # 홀수
            return mult_matrix(n, mult_matrix(n, tmp, tmp), matrix)


n, b = map(int, (input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = solution(n, b, matrix)

for row in ans:
    for num in row:
        print(num % 1000, end=" ")
    print()


# 경우의 수 같은 곳에 많이 나옴 -> 반으로 분할하여 함 -> 홀수 짝수
