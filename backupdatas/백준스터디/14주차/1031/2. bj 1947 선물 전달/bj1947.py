# 백준 1890. 선물 전달
import sys
sys.stdin = open("bj1947input.txt")

dp = [0] * (1000001)
dp[2] = 1
dp[3] = 2
for i in range(4, 1000001):
    dp[i] = (dp[i-1]+dp[i-2]) * (i-1) % 1000000000
# 원래 T는 없음
T = int(input())
for tc in range(T):
    N = int(input())
    print(dp[N])