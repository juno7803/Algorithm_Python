from sys import stdin
input = stdin.readline

n = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0

for i in range(n):
    if(i < n-1):
        if (price[i] < price[i+1]):
            price[i+1] = price[i]
        total += price[i] * city[i]
print(price)
