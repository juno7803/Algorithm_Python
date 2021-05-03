from sys import stdin
from math import factorial
input = stdin.readline

n, k = map(int, input().split())


def sol():
    if k < 0 or k > n:
        print(0)
    else:
        print(int(factorial(n) / (factorial(k)*factorial(n-k))))


sol()
