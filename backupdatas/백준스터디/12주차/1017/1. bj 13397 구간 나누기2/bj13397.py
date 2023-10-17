# 백준 13397. 구간 나누기 2
import sys
sys.stdin = open("bj13397input.txt")


# T는 원래 없음
T = int(input())
for tc in range(T):
    # N : 1차원 배열의 원소 개수(1 <= N <= 5000)
    # M : 구간의 개수(1 <= M <= N)
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_v = 0
    max_v = max(arr)
    while min_v <= max_v:
        # 현재 구간 정의시, mid값을 최대의 구간 점수로 만드려고 함
        mid = (min_v+max_v)//2
        c = 1

        idx = 0
        for i in range(idx, N):
            # idx ~ i까지 구간 점수
            val = max(arr[idx:i+1])-min(arr[idx:i+1])
            # 구간 점수가 목표 구간 점수 최대값보다 커질 경우, 구간 나누기(~(i-1)까지만)
            if val > mid:
                c += 1
                idx = i
        # 현재 mid값을 최대 구간 점수로 둘 경우, 조건 성립 -> mid값을 더 낮춰보기
        # 목표 : 최대 구간 점수가 최소가 될 경우
        if c <= M:
            # min_v = mid+1
            max_v = mid-1
        # 현재 mid값을 최대 구간 점수로 둘 경우, M개보다 더 많은 구간 발생 -> mid값을 더 높여보기
        else:
            # max_v = mid-1
            min_v = mid+1
    print(min_v)