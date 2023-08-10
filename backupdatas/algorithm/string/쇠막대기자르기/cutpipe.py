# 쇠막대기 자르기
import sys
sys.stdin = open("cutpipeinput.txt")
T = int(input())
for test_case in range(1, T+1):
    string = input()
    # 잘린 총 개수
    result = 0
    # 현재 쇠파이프 개수
    c = 0
    for i in range(len(string)):
        # 쇠파이프 시작 or 레이저
        if string[i] == '(':
            c += 1
        # 쇠파이프 끝 or 레이저 끝
        else:
            # 레이저인 경우
            if string[i-1] == '(':
                # 쇠파이프 개수 하나 제거
                c -= 1
                # 지금까지 따라온 쇠파이프(잘린 쇠파이프) 개수만큼
                result += c
            # 쇠파이프의 끝인 경우
            else:
                # 자투리 추가 및 쇠파이프 개수 제거
                result += 1
                c -= 1
    print(f'#{test_case} {result}')







''' 
내가 짠 코드(시간초과)           
import sys
sys.stdin = open("cutpipeinput.txt")
T = int(input())
for test_case in range(1, T+1):
    string = input()
    result = 0

    for i in range(len(string)-1):
        # 1. '()' 를 찾은 경우
        if string[i] == '(':
            if string[i+1] == ')':
                for j in range(i):
                    if string[j] == '(':
                        result += 1
                    if string[j] == ')':
                        result -= 1
        # 2. ')('를 찾은 경우
        else:
            if string[i+1] == '(':
                idx = i
                while string[idx] == ')':
                    idx -= 1
                result += (i-idx-1)
    # 마지막 자투리 개수
    idx = 0
    for i in range(len(string)-1):
        if string[i] == '(':
            idx = i
    result += (len(string)-idx-2)
    print(f'#{test_case} {result}')
'''



