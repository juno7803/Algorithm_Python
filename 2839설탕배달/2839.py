n = int(input()) # 설탕 무게
bags = 0 # 봉지 수

while True: 
    if n % 5 == 0: # 5로 나눠떨어지면(5와 3중 큰것으로 먼저 나눔)
        bags += n//5 # bag += 몫
        print(bags)
        break
    else:
        n -= 3 # 남은 무게는 3키로로 채움
        bags += 1
    if n < 0: # 초과해서 뺀 경우
        print(-1)
        break
    elif n == 0: # 딱 맞춘 경우
        print(bags)
        break