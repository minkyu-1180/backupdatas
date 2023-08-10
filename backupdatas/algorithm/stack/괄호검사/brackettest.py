# 괄호 검사
import sys
sys.stdin = open("brackettestinput.txt")

# push 함수
def push(stack, item):
    global top
    top += 1
    stack.append(item)
    return

# pop 함수
def pop():
    global top
    popitem = stack.pop(top)
    top -= 1
    return popitem


T = int(input())
for test_case in range(1, T+1):
    string = input()

    stack = []
    top = -1
    result = 1
    i = 0

    while i < len(string):
        # 현재 스택의 상태가 비어있는 경우
        if stack == []:
            if string[i] == '(' or string[i] == '{':
                push(stack, string[i])
            # 비어있는데 짝이 없는 오른쪽 볼록이 온 경우
            elif string[i] == ')' or string[i] == '}':
                result = 0
                break

        # 현재 스택에 들어가 있는 경우
        else:
            # 현재 참조값이 왼쪽 볼록인 경우 : push
            if string[i] == '(' or string[i] == '{':
                push(stack, string[i])

            # 오른쪽 볼록이면 stack의 top 값과 비교하여 짝인지 확인
            elif string[i] == ')':
                if stack[top] == '(':
                    pop()
                else:
                    result = 0
                    break

            elif string[i] == '}':
                if stack[top] == '{':
                    pop()
                else:
                    result = 0
                    break
        i += 1


    if len(stack) != 0:
        result = 0
    print(result)



'''
    for i in range(len(string)):
        # 현재 스택의 상태가 비어있는 경우
        if stack == []:
            if string[i] == '(' or string[i] == '{':
                push(stack, string[i])
            # 비어있는데 짝이 없는 오른쪽 볼록이 온 경우
            elif string[i] == ')' or string[i] == '}':
                result = 0
                break

        # 현재 스택에 들어가 있는 경우
        else:
            # 현재 참조값이 왼쪽 볼록인 경우 : push
            if string[i] == '(' or string[i] == '{':
                push(stack, string[i])

            # 오른쪽 볼록이면 stack의 top 값과 비교하여 짝인지 확인
            elif string[i] == ')':
                if stack[top] == '(':
                    pop()
                else:
                    print(f'#{test_case} 0')
                    break

            elif string[i] == '}':
                if stack[top] == '{':
                    pop()
                else:
                    print(f'#{test_case} 0')
                    break
    # 짝이 안 맞는 문제는 없었지만, 홀수 개수라서 stack 안에 남아있는 경우
'''