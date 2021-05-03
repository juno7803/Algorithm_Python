from sys import stdin
input = stdin.readline

n, m = map(int, input().split())  # n : 사람의 수, m : 파티의 수
truth = list(map(int, input().split()))
truth_list = set(truth[1:])
party_list = [[] for _ in range(m+1)]

for _ in range(m):
    party = list(map(int, input().split()))
    party_list[party[0]] = party[1:]
