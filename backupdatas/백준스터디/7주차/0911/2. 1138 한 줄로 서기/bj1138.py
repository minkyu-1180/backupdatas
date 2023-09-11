# 백준 1138. 한 줄로 서기
import heapq
import sys
sys.stdin = open("bj1138input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = [0] * N
    idx = 0
    rest = []
    while idx < N:
        v = arr[idx]
        # 본인 앞에 더 큰게 X -> 가장 앞에 나오는 0에 삽입
        if v == 0:
            for i in range(N):
                if result[i] == 0:
                    result[i] = idx + 1
                    break
        else:
            c = 0
            for i in range(N):
                if result[i] == 0:
                    c += 1
                    if c > v:
                        result[i] = idx + 1
                        break
        idx += 1

    for i in range(N):
        print(result[i], end = ' ')
    print()




