# 백준 1010. 다리 놓기
import sys
sys.stdin = open("bj1010input.txt")

dp = [[0] * (31) for _ in range(31)]
for i in range(1, 31):
    for j in range(1, 31):
        if i == 1:
            dp[i][j] = j
        elif i == j:
            dp[i][j] = 1
        elif i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]



T = int(input())
for tc in range(T):
    # N : 서쪽 다리 개수
    # M : 동쪽 다리 개수
    N, M = map(int, input().split())
    # dp[i][j] : 서쪽에 j, 동쪽에 i개 있을 때의 놓는 방법 수
    print(dp[N][M])