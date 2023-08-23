# sw academy 이진수
import sys
sys.stdin = open("이진수input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, N_str = input().split()
    result = ''
    for num in N_str:
        # 10 ~ 15
        if 'A' <= num <= 'F':
            num = ord(num) - 55 # 16비트연산값 -> 10진수
        # 0 ~ 9
        else:
            num = int(num)

        two_str = ''
        # 10진수를 2진수로 바꾸는 방법
        while num:
            rest = num % 2
            two_str = str(rest) + two_str
            num = num // 2

        # 8보다 값이 작아서 앞의 0이 채워지지 않은 경우
        while len(two_str) < 4:
            two_str = '0' + two_str
        result += two_str
    print(f'#{test_case} {result}')