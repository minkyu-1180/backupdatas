# 반복문자 지우기
import sys
sys.stdin = open("erasestringinput.txt")

T = int(input())

# top 설정

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



for test_case in range(1, T+1):
    string = input()
    # 반복해서 돌 문자열의 길이 / top / stack 초기화
    N = len(string)
    top = -1
    stack = []


    for i in range(N):
        # stack이 비어있는 경우
        # i = 0 or 모든 stack 요소들에 대해 pop이 이루어진 경우
        if stack == []:
            push(stack, string[i])
            # print(f'push 실행 : top - {top}, i - {i}, push한 값 : {stack[top]}')
        # stack 안에 string의 문자와 비교할 대상이 있는 경우
        else:
            # 같을 경우 -> 빼내야됨 : pop
            if stack[top] == string[i]:
                pop()
                # print(f'pop 실행 : top - {top}, i - {i}')
            # 다를 경우 -> 빼낼 필요 X : push
            elif stack[top] != string[i]:
                push(stack, string[i])
                # print(f'push 실행 : top - {top}, i - {i}, push한 값 : {stack[top]}')
    result = len(stack)
    print(f'#{test_case} {result}')




