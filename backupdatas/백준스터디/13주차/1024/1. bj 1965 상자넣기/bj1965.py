# 백준 1965. 상자넣기
import sys
sys.stdin = open("bj1965input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 상자 개수(1 <= N <= 1000)
    N = int(input())
    # 각 상자의 크기를 순서대로 담은 것
    arr = list(map(int, input().split()))
    # dp[i] : 앞에 있는 상자들 중, 담을 수 있는 상자 개수
    # 자기 자신 포함 -> 1로 초기화
    dp = [1] * N
    for i in range(1, N):
        max_v = 0
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i] and max_v < dp[j]:
                max_v = dp[j]
        dp[i] += max_v
    print(max(dp))

