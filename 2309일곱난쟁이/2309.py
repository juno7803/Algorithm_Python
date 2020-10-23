key = []
for _ in range(9):
    key.append(int(input()))

diff = sum(key) - 100
for i in range(9):
    for j in range(i+1, 9):
        if ((key[i] + key[j]) == diff):
            wrong1 = key[i]
            wrong2 = key[j]
key.remove(wrong1)
key.remove(wrong2)
key.sort()

for i in key:
    print(i)
    