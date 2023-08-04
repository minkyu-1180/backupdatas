
import sys
sys.stdin = open("input.txt")
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row_c = 0

    # 1. 열 별로 파악
    # i : arr의 row 번호
    for i in range(N):
        # 벽이 있는 경우(j == 0) : 왼쪽 벽
        if arr[i][0] == 1:
            k_list = [arr[i][k] for k in range(K)]
            if 0 not in k_list:
                if arr[i][K] == 0:
                    row_c += 1
        # 벽이 있는 경우(j == K) : 오른쪽 벽
        if arr[i][N-K] == 1:
            k_list = [arr[i][N-K + k] for k in range(K)]
            if 0 not in k_list:
                if arr[i][N-K-1] == 0:
                    row_c += 1

        # j : arr의 col 번호
        for j in range(1, N-K):
            # k_list : arr[i][j] ~ arr[i][j+K-1]까지 담은 리스트
            k_list = [arr[i][j + k] for k in range(K)]
            # jth index값 기준으로 k개의 요소들이 다 1로 차있는 경우(글자를 적을 수 있는 길이 있을 때)
            if 0 not in k_list:
                # (j-1), (j+K)th ele 확인
                if arr[i][j-1] == 0 and arr[i][j+K] == 0:
                    row_c += 1

    # 증가가 안 된 곳 : 6번 행의 j = 1 case
    # 증가가 안 된 곳 : 8번 행의 j = N-1 case(근데 j = 0 case는 되었음)

    # 2. 행 별로 파악
    # j : arr의 col 번호
    col_c = 0
    for j in range(N):
        # 벽이 있는 경우(i == 0) : 왼쪽 벽
        if arr[0][j] == 1:
            k_list = [arr[k][j] for k in range(K)]
            if 0 not in k_list:
                if arr[K][j] == 0:
                    col_c += 1

        # 벽이 있는 경우(i == K) : 오른쪽 벽
        if arr[N-K][j] == 1:
            k_list = [arr[N - K + k][j] for k in range(K)]
            if 0 not in k_list:
                if arr[N - K - 1][j] == 0:
                    col_c += 1

        # j : arr의 col 번호
        for i in range(1, N - K):
            # k_list : arr[i][j] ~ arr[i][j+K-1]까지 담은 리스트
            k_list = [arr[i+k][j] for k in range(K)]
            # jth index값 기준으로 k개의 요소들이 다 1로 차있는 경우(글자를 적을 수 있는 길이 있을 때)
            if 0 not in k_list:
                # (j-1), (j+K)th ele 확인
                if arr[i-1][j] == 0 and arr[i+K][j] == 0:
                    col_c += 1

    result = row_c + col_c
    print(f'#{test_case} {result}')
