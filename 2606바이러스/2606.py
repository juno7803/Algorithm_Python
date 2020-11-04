from sys import stdin

n = int(stdin.readline())
e_num = int(stdin.readline()) # 실제 연결된 갯수
adj = [list() for i in range(n+1)] # 인접 리스트 n+1 : 0번째 인덱스는 쓰지 않기 위함
chk = [0 for i in range(n+1)] # check 배열 [0,0,...] 방문했으면 1로 변경

for i in range(e_num): 
    a,b = map(int,stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(x):
    chk[x] = 1
    for i in range(len(adj[x])):
        tmp = adj[x][i]
        if(chk[tmp] == 0):
            dfs(tmp)

dfs(1)
cnt = -1
for i in chk:
    if i == 1:
        cnt += 1
print(cnt)