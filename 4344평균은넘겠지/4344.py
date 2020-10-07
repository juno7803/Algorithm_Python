for i in range(int(input())):
    score = list(map(int,input().split()))
    num = score[0]  # 학생 수
    avg = sum(score[1:]) / num  # 평균
    overAvg = 0 # 평균 넘는 학생 수
    for i in score[1:]:
        if i > avg:
            overAvg += 1
    rate = (overAvg / num) * 100
    print(format(round(rate,3),".3f")+"%")
    # 또는 다음과 같이 활용 가능 print("{0:.3f}".format(round(rate,3))+"%")
