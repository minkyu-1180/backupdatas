# sw academy 계산기 1
import sys
sys.stdin = open("operator1input.txt")
for test_case in range(1, 11):
    N = int(input())
    arr = list(input())

    stack = []
    back_string = []
    for s in arr:
        if s != '+':
            back_string.append(s)
        else:
            if stack == []:
                stack.append(s)
            else:
                back_string.append(stack.pop())
                stack.append(s)
    back_string.append(stack.pop())
    # print(back_string)

    for s in back_string:
        if s == '+':
            if stack:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 + num2)
            else:
                stack.append(s)
        else:
            stack.append(s)
    print(f'#{test_case} {stack[0]}')