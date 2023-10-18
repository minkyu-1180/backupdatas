# 백준 1561. 놀이 공원
import sys
sys.stdin = open("bj1561input.txt")
from collections import defaultdict

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 아이들의 수(1<=N<=2000000000)
    # M : 놀이기구 개수(1<=M<=10000)
    N, M = map(int, input().split())
    # arr[i] : i번 놀이기구의 한 번 운행 시간(분)
    arr = [0] + list(map(int, input().split()))
    if N <= M:
        print(N)
    else:
        noligigu = [[] for _ in range(31)]
        for i in range(1, M+1):
            time = arr[i]
            noligigu[time].append(i)

        min_time = 1
        max_time = max(arr) * N