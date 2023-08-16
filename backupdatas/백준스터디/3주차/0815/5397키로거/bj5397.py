# 백준 5397. 키로거
import sys
sys.stdin = open("5397input.txt")
T = int(input())
for test_case in range(1, T+1):
    arr = list(input()) # 길이가 L(1 <= L <= 1000000)인 문자열
    '''
    조건
    백스페이스입력 시 : '-'
    화살표 입력 : '<' or '>'
    - 커서의 위치를 움직일 수 있는 경우, 왼쪽 또는 오른쪽으로 1만큼 움직임
    - 커서의 시작 : 0번 idx
    '''
    stack1 = [] # 새로운 문자 append
    stack2 = [] # 뒤집을거

    for s in arr:
        if s not in '<>-':
            stack1.append(s)
        else:
            if s == '-' and stack1:
                stack1.pop()

            elif s == '<' and stack1:
                stack2.append(stack1.pop())

            elif s == '>' and stack2:
                stack1.append(stack2.pop())

    stack1.extend(reversed(stack2))
    print(''.join(stack1))