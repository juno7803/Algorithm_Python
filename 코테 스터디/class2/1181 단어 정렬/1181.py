from sys import stdin
input = stdin.readline

n = int(input())
word = [input().rstrip('\n') for _ in range(n)]

word = list(set(word))
word.sort()
word.sort(key=lambda x: (len(x), x))
print('\n'.join(word))
