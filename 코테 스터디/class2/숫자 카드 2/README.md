### 10816번 숫자 카드 2

** 처음 시도한 방법**

- filter + lambda를 통한 같은 수 여러개 찾기
- 시간초과로 실패

```python
result = []
for ele in ans:
    q = list(filter(lambda x: sol[x] == ele, range(len(sol))))
    result.append(len(q))

print(*result)
```

** 두번째 시도한 방법 **

- 처음엔 이분탐색을 시도하려고 하였으나, 어차피 이분탐색도 여러개를 찾아야 하므로, `O(log(n))`이 여러번 반복될거라 생각함
- `dictory(hash)`를 사용하여 key를 통해 갯수를 찾아 `O(1)` (고유한 key에 해당하는 항목을 찾으므로) 이 여러번 반복되므로 시간초과가 나오지 않음

```python
dict = {} # 중괄호를 통해 딕셔너리 생성

for s in sol:
    if(s in dicts):
        dicts[s] += 1
    else:
        dicts[s] = 1
# 딕셔너리의 같은 key에 value를 늘려가며 저장한다.
```
