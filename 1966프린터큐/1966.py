for _ in range(int(input())): # 테스트 케이스
    n,m = list(map(int,input().split())) # n과 m 채우기
    imp = list(map(int,input().split())) # 큐에 들어간 중요도
    order = list(range(n))
    order[m] = -1 # target의 order를 -1로 지정
    count = 0

    while True:
        if imp[0] == max(imp): # 최댓값이면 order+=1
            count += 1
            if order[0] == -1: # target이면 출력 후 where 탈출
                print(count)
                break
            else:
                imp.pop(0) # python의 pop은 인덱스를 지정하여 뺄 수 있다.(반드시 마지막 원소가 아님)
                order.pop(0)
        else:
            imp.append(imp.pop(0))
            order.append(order.pop(0)) 