s = int(input())
n = 1

while n*(n+1)/2 <= s: # s보다 커질때까지 n을 더한다
    n += 1
if(n*(n+1)/2 == s): # 같을 경우 1 출력
    print(n)
else:
    print(n-1)