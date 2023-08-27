# IM 대비 20. 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open("단어input.txt")
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # 1. row별로 개수 찾기
    for i in range(N):
        for j in range(N):
            # 1을 만났을 경우
            if arr[i][j] == 1:
                if (j > 0 and arr[i][j-1] == 0) or (j == 0):
                    if j + K - 1 < N:
                        if j + K - 1 == N-1:
                            if [arr[i][j+l] for l in range(K)] == [1] * K:
                                result += 1
                        elif ([arr[i][j+l] for l in range(K)] == [1] * K) and arr[i][j+K] == 0:
                            result += 1

    # 2. col별로 개수 찾기
    for j in range(N):
        for i in range(N):
            # 1을 만났을 경우
            if arr[i][j] == 1:
                if (i > 0 and arr[i-1][j] == 0) or (i == 0):
                    if i + K - 1 < N:
                        if i + K - 1 == N-1:
                            if [arr[i+l][j] for l in range(K)] == [1] * K:
                                result += 1
                        elif ([arr[i+l][j] for l in range(K)] == [1] * K) and arr[i+K][j] == 0:
                            result += 1
    print(f'#{test_case} {result}')







