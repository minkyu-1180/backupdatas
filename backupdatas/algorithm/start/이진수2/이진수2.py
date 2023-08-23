# sw academy 이진수2
import sys
sys.stdin = open("이진수2input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    i = 1 # 소수 i번쨰
    result = ''
    while i < 13:
        if N - 2 **(-i) >= 0:
            N -= 2 ** (-i)
            result += '1'
            i += 1
        else:
            result += '0'
            i += 1
        # N이 0이된 경우(특정 소수 i번째까지 2진수로 표현 가능한 경우)
        if N == 0:
            break
    if N != 0:
        result = 'overflow'
    print(f'#{test_case} {result}')