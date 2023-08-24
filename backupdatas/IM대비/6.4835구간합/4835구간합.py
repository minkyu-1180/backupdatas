# IM 대비 6. 구간합
import sys
sys.stdin = open("구간합input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 정수 개수(10 <= N <= 100)
    # M : 구간 크기 (2 <= M < N)
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = [0] * (N-M+1)

    # result[i] : i번 ~ i + M - 1번 값의 합(구간합)
    for i in range(N-M+1):
        # i번 idx의 값을 시작으로 M개의 연속된 수의 합을 담을 변수
        m_sum = 0
        # i ~ i + M - 1까지의 합
        for j in range(i, i + M):
            m_sum += arr[j]
        result[i] = m_sum

    max_v = result[0]
    min_v = result[0]
    for val in result:
        if max_v < val:
            max_v = val
        if min_v > val:
            min_v = val
    ans = max_v - min_v
    print(f'#{test_case} {ans}')