def func():
    for i in range(int(input())):
        flag = True # ')'가 들어왔는데, 스택이 빈 경우 False 처리
        stack = []
        bracket = list(input())
        for i in bracket:
            if(i == '('):
                stack.append(i)
            else:
                if len(stack) == 0:
                    print("NO")
                    flag = False
                    break
                else:
                    stack.pop()
        if flag == False:
            pass
        else:
            if len(stack) == 0:
                print("YES")
            else:   
                print("NO")

func()