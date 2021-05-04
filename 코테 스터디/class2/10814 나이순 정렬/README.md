### 10814 나이순 정렬

- python에서 입력을 어떻게 받는지와, `sort(key=lambda x:())` 를 어떻게 활용하냐를 묻는 문제
- 한번 틀렸었는데, 이는 `string`으로 받아온 나이를 `lambda`에서 비교할 때 `int`로 형 변환해서 비교를 하지 않아서 틀렸었음

```python
    sort(arr,key=lambda x: (int(x[0]),x[2]))
```
