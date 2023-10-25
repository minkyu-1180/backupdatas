# 백준 15989. 1, 2, 3, 그리고 4
import sys
sys.stdin = open("bj15989input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    if N <= 3:
        print(N)

    else:
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, 6):
            dp[i] = i
        for i in range(6, N+1):
            dp[i] = dp[i-6] + i
        print(dp[N])