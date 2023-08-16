# sw academy 계산기 2
import sys
sys.stdin = open("operator2input.txt")

for test_case in range(1, 11):
    N = int(input())
    string = list(input())

    # 연산자를 담을 스택
    stack = []
    # 후위표기법
    back_string = []
    for s in string:

        if s not in '+*':
            back_string.append(s)
        else:
            if s == '+' and stack:
                while stack:
                    back_string.append(stack.pop())

            stack.append(s)
    while stack:
        back_string.append(stack.pop())



    new_stack = []
    for s in back_string:
        if s not in '+*':
            new_stack.append(s)
        else:
            num2 = int(new_stack.pop())
            num1 = int(new_stack.pop())
            if s == '+':
                new_stack.append(num1 + num2)
            else:
                new_stack.append(num1 * num2)
    print(f'#{test_case} {new_stack[0]}')
