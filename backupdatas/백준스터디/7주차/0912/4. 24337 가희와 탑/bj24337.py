# # 백준 24337. 가희와 탑
import sys
sys.stdin = open("bj24337input.txt")
T = int(input())
for tc in range(T):
    N, a, b = map(int, input().split())

    if a + b - 1 >= N:
        print(-1)
    else:
        max_v = max(a, b)
        result = [0] * N

        result[N-b] = max_v
        # print(result)

        for i in range(1, b):
            result[N-i] = i
        # print(result)

        for i in range(1, a):
            result[N-b-(a-i)] = i
        # print(result)

        for i in range(N-a-b+1):
            result[i] = 1
        print(result)

