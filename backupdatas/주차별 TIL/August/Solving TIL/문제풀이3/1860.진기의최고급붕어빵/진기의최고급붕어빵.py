# 진기의 최고급 붕어빵
import sys
sys.stdin = open("진기의최고급붕어빵input.txt")
T  = int(input())
for test_case in range(1, T+1):
    # N : 먹을 자격이 있는 사람 수
    # M : 시간(초)
    # K : M초동안 만든 붕어빵 개수(0초부터 만들기 시작)
    # 1 <= N, M, K <= 100
    N, M, K = map(int, input().split())
    # 각 사람이 언제 도착하는지 초 단위로 주어지는 배열
    # 0 <= val <= 11111
    arr = list(map(int, input().split()))
    arr.sort()
    result = 'Possible'
    for i in range(N):
        if i + 1 > arr[i]//M*K:
            result = 'Impossible'
            break
    print(f'#{test_case} {result}')