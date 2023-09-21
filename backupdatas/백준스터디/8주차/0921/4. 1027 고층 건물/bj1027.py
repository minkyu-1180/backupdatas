# 백준 1027. 고층 건물
import sys
sys.stdin = open("bj1027input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int ,input().split()))
    result = 0
    idx = 0
    while idx < N:
        # 작은 쪽
        if idx > 0:
            c1 = 1
            slope1 = arr[idx] - arr[idx-1]
            for i in range(idx-1, -1, -1):
                now_slope = (arr[idx] - arr[i])/(idx-i)
                if slope1 > now_slope:
                    slope1 = now_slope
                    c1 += 1
        else:
            c1 = 0

        if idx < N-1:
            c2 = 1
            slope2 = arr[idx+1] - arr[idx]
            for i in range(idx+1, N):
                now_slope = (arr[i] - arr[idx])/(i-idx)
                if slope2 < now_slope:
                    slope2 = now_slope
                    c2 += 1
        else:
            c2 = 0

        if result < c1+c2:
            result = c1+c2
        idx += 1

    print(result)