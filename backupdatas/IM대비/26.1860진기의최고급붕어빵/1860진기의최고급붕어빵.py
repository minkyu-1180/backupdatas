# IM 대비 26. 진기의 최고급 붕어빵
import sys
sys.stdin = open("붕어빵input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort() # 오는 시간 정렬

    result = 'Possible'
    for t in range(N):
        # 현재 만들어진 빵 - 손님 수(누적)
        bbang = (arr[t]//M) * K - (t+1)
        if bbang < 0:
            result = 'Impossible'
            break
    print(f'#{test_case} {result}')
