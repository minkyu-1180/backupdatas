# 백준 10164. 격자상의 경로
import sys
sys.stdin = open("bj10164input.txt")

def dp(N, M):
    memo = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1  and j == 1:
                memo[i][j] = 1
                continue
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
    return memo[N][M]

T = int(input())
for tc in range(T):
    # N : 행의 수
    # M : 열의 수 (1 <= N, M <= 15)
    # K : O로 표시된 칸의 번호(0 <= K <= NXM)
    N, M, K = map(int, input().split())
    # 중간 만나는 지점
    k_i = (K-1)//M + 1
    k_j = K - (k_i-1) * M
    # 결과 좌표
    e_i, e_j = N-(k_i-1), M-(k_j-1)

    if K == 0:
        result = dp(N, M)
    else:
        result = dp(k_i, k_j) * dp(e_i, e_j)
    print(result)

