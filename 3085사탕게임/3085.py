import sys
N = int(sys.stdin.readline())
candy = [list(map(str, input())) for _ in range(N)] # 2차원 배일 in python

def chk(c): # candy 중에서 최대 겹치는 갯수 알려줌
    ans = 1
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if c[i][j] == c[i][j-1]: # 행
                cnt += 1
            else:
                cnt = 1 # 연속이 끝나면 1로 초기화
            ans = max(ans,cnt) # 최대 연속 수 ans 저장
        cnt = 1
        for j in range(1,N):
            if c[j][i] == c[j-1][i]: # 열
                cnt+=1
            else:
                cnt = 1
            ans = max(ans,cnt)
    return ans

ans = 0
for i in range(N):
    for j in range(N):
        if j+1 < N: # 오른쪽 검사
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j] # swap
            tmp = chk(candy)
            ans = max(ans,tmp)
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j] # 원래대로
        if i + 1 < N: # 아랫쪽 검사
            candy[i][j],candy[i+1][j] = candy[i+1][j],candy[i][j]
            tmp = chk(candy)
            ans = max(ans,tmp)
            candy[i][j],candy[i+1][j] = candy[i+1][j],candy[i][j]

print(ans)