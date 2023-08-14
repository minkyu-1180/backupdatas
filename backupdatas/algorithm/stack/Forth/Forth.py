import sys
sys.stdin = open("Forthinput.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input().split())
    stack = []
    isoper = '+-*/.'

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