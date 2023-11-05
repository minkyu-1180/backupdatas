# 백준 11047. 동전 0
import sys
sys.stdin = open("bj11047input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 동전의 종류(1 <= N <= 10)
    # K : 가치의 합 목표 (1 <= K <= 100000000)
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    result = 0
    last = K
    idx = N-1
    while idx >= 0:
        c = last//arr[idx]
        last -= c * arr[idx]
        result += c
        if last == 0:
            break
        idx -= 1
    print(result)