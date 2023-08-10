# 회문
import sys
sys.stdin = open("reversesameinput.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 열 별로 회문 찾기
    for i in range(N):
        # 행
        for j in range(N-M+1):
            jth_arr = [0] * M
            isreversesame = [0] * M
            # jth ~ (j+M-1)th 인덱스 요소
            for k in range(M):
                jth_arr[k] = arr[i][j+k]
                isreversesame[k] = arr[i][j+M-1-k]
            if jth_arr == isreversesame:
                result = "".join(jth_arr)

        # 행 별로 회문 찾기
        for j in range(N):
            # 열
            for i in range(N - M + 1):
                ith_arr = [0] * M
                isreversesame = [0] * M
                # ith ~ (i+M-1)th 인덱스 요소
                for k in range(M):
                    ith_arr[k] = arr[i+k][j]
                    isreversesame[k] = arr[i + M - 1 - k][j]
                if ith_arr == isreversesame:
                    result = "".join(ith_arr)
    print(f'#{test_case} {result}')
