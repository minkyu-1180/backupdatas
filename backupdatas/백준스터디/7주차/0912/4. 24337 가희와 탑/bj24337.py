# # 백준 24337. 가희와 탑
import sys
sys.stdin = open("bj24337input.txt")
T = int(input())
for tc in range(T):
    N, a, b = map(int, input().split())

    if a + b - 1 > N:
        print(-1)
    else:
        result = [0] * N
        # a = 1
        if a == 1:
            for i in range(b):
                result[i] = b-i
            for i in range(b, N):
                result[i] = 1
        # b = 1
        elif b == 1:
            idx = 1
            for i in range(N-a, N):
                result[i] = idx
                idx += 1
            for i in range(N-a):
                result[i] = 1


        else:
            max_v = max(a, b)

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

        for i in range(N):
            print(result[i], end = ' ')
        print()
