# 백준 3709. 입국심사
import sys
sys.stdin = open("bj3709input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 심사대의 개수 (1 <= N <= 100000)
    # M : 사람 수 (1 <= M <= 1000000000)
    N, M = map(int, input().split())
    # arr[i] : i번 심사대에서 심사 받는 데 걸리는 시간
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    # 현재 i번에 있는지 없는지
    min_time = 1
    max_time = max(arr) * M
    result = 0
    while min_time <= max_time:
        mid = (min_time+max_time)//2

        # mid의 시간동안 총 몇명의 사람이 심사를 통과할 수 있을까?
        c = 0
        for num in arr:
            c += mid//num
        # 시간 안에 M명보다 더 많이 통과 가능 -> good case
        # 시간을 더 줄여보자
        if c >= M:
            max_time = mid-1
            result = mid
        # M명을 심사 완료하기 위해서는 더 많은 시간 필요
        else:
            min_time = mid+1
    print(result)

