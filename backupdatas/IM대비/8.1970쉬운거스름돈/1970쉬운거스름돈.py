# IM 대비 8. 쉬운 거스름돈
import sys
sys.stdin = open("거스름돈input.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 거스름돈(10 <= N <= 100000)
    s_market = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    result = [0] * 8
    # 가장 큰 거스름돈으로 최대한 걸러주기
    idx = 0
    # 더이상 거슬러줘야 할 금액이 없을 때 종료
    while N > 0:
        # 현재 돈 종류로 거슬러 줄 수 있는 최대 개수
        c = N // s_market[idx]
        result[idx] = c # idx에 해당하는 돈 종류 개수
        N -= c * s_market[idx] # 거슬러주고 남은 거스름돈
        idx += 1
        if N < 10:
            break
    print(f'#{test_case}')
    print(*result)



