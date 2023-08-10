# 9012. 괄호
import sys
sys.stdin = open("9012input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    for _ in range(N):
        string = input()
        result = 0
        K = len(string) // 2
        c = 0
        # 횟수는 원본 배열의 길이의 절반에 다다를 때 까지
        while c < K:
            # 현재 string의 VPS 제거 후 반환
            string = string.replace('()', '')
            # 카운트 증가
            c += 1
            # 반환 후 길이가 0 or 1일 경우 종료(더 이상 replace 불가)
            if len(string) <= 1:
                break
        if len(string) == 0:
            print('YES')
        else:
            print('NO')
