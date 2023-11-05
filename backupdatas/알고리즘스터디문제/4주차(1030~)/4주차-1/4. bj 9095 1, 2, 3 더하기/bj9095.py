# 백준 9095. 1, 2, 3 더하기
import sys
sys.stdin = open("bj9095input.txt")

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(dp[N])