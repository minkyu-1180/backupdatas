# IM 대비 5. 백준 2559 수열
import sys
sys.stdin = open('2559수열input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N : 총 온도 잰 횟수 (2 <= N <= 100000)
    # K : 구간합(1 <= K <= N)

    N, K = map(int, input().split())
    # 온도(-100 ~ 100)
    arr = list(map(int, input().split()))
    result = [0] * (N-K+1)

    # 초기값 설정
    c = 0
    for i in range(K):
        c += arr[i]
    result[0] = c

    for i in range(1, N-K+1):
        result[i] = result[i-1] - arr[i-1] + arr[i+K-1]

    print(max(result))
