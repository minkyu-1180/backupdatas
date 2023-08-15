import sys
sys.stdin = open("Forthinput.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input().split())

    # print(arr)
    stack = []
    operator = '+-*/'
    for s in arr:
        if s == '.':
            if len(stack) == 1:
                print(f'#{test_case} {stack[0]}')
            else:
                print(f'#{test_case} error')

        elif s not in operator:
            stack.append(int(s))
            # print(f'stack : {stack}')
        else:
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if s == '+':
                    stack.append(num1 + num2)
                if s == '-':
                    stack.append(num1 - num2)
                if s == '*':
                    stack.append(num1 * num2)
                if s == '/':
                    if num2 != 0:
                        stack.append(num1 // num2)
                    else:
                        print(f'#{test_case} error')

'''
    for s in arr:
        if s not in isoper:
            stack.append(s)
        elif s == '+':
            if len(stack) < 4:
                num2 = str(stack.pop())
                num1 = str(stack.pop())
                if num1 in isoper or num2 in isoper:
                    print(f'#{test_case} error')
                    break
            elif len(stack)
            else:
                num = int(num1) + int(num2)
                stack.append(num)
        elif s == '-':
            num2 = str(stack.pop())
            num1 = str(stack.pop())
            if num1 in isoper or num2 in isoper:
                print(f'#{test_case} error')
                break
            else:
                num = int(num1) - int(num2)
                stack.append(num)
        elif s == '*':
            num2 = str(stack.pop())
            num1 = str(stack.pop())
            if num1 in isoper or num2 in isoper:
                print(f'#{test_case} error')
                break
            else:
                num = int(num1) * int(num2)
                stack.append(num)
        elif s == '/':
            num2 = str(stack.pop())
            num1 = str(stack.pop())
            if num1 in isoper or num2 in isoper:
                print(f'#{test_case} error')
                break
            else:
                num = int(num1) / int(num2)
                stack.append(num)
        elif s == '.':
            print(f'#{test_case} {stack[0]}')
'''