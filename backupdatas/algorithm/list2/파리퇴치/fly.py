# sw academy extra - 파리퇴치
import sys
sys.stdin = open("flyinput.txt")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # sum_matrix1의 (i, j) 인덱스 값은
    # 받은 matrix의 (i, j) ~ (i, j + M - 1)까지의 합
    sum_matrix = [[0] * (N-M+1) for _ in range(N)]

    # sum_matrix 업데이트
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                sum_matrix[i][j] += arr[i][j+k]

    # result[i][j] : (i, j)번 index의 요소부터 (i+M-1, j+M-1)번 index 요소까지의 합
    result_list = [[0] * (N-M+1) for _ in range(N-M+1)]
    for j in range(N-M+1): # j = 0, 1, 2,,, N-M
        for i in range(N-M+1):
            for k in range(M):
                result_list[i][j] += sum_matrix[i+k][j]

    # 최대 값을 담을 변수
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if result < result_list[i][j]:
                result = result_list[i][j]
    print(f'#{test_case} {result}')



