# 백준 2839. 설탕 배달
import sys
sys.stdin = open("2839input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    c =0

    while N >= 0:
        # N이 5의 배수일 경우(최적)
        if N % 5 == 0:
            c += N // 5
            print(c)
            break
        # 5의 배수가 아닐 경우 -> 최대한 3으로 진행
        N -= 3
        c += 1

        if N < 0:
            print(-1)
            break
