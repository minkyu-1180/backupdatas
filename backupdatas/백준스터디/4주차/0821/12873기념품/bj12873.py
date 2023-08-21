# 백준 12873. 기념품
import sys
sys.stdin = open("12873input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 참가자 수 : 1 ~ 5000
    '''
    1단계 : 1
    2단계 : 2 ~ 2^3
    3단계 : 2^3 + 1 ~ 3^3
    4단계 : 3^3 + 1 ~ 4^3....
    '''
    arr = list(range(1, N+1))
    top = 0 # 숫자를 세주기 시작할 인덱스 위치
    for i in range(1, N):
        top = (top + (i**3) - 1)% len(arr) # out of range 방어

        if top == -1: # top = i = 0 case
            top += len(arr)
        arr.pop(top)
    print(arr[0])