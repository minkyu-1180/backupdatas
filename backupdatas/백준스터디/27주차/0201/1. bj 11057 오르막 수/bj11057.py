# 백준 11057. 오르막 수
import sys
sys.stdin = open("bj11057input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    N = int(input())
    # 길이가 N인 수 중, 오르막 수의 개수
    # dp[i][j] : 길이가 i인 수 중, 가장 앞 글자가 j인 오르막 수의 개수
    # 가장 앞 글자가 j인 i-1짜리 ~ 9인 i-1짜리
    dp = [[0] * 10 for _ in range(N+1)]
    dp[1] = [1] * 10

    if N >= 2:
        for i in range(2, N+1):
            for j in range(10):
                for k in range(j, 10):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % 10007
    print(sum(dp[N])%10007)