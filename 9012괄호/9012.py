def func():
    for i in range(int(input())):
        flag = True
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