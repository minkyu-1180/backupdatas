# 백준 1309. 동물원
import sys
sys.stdin = open("bj1309input.txt")

# 동물원 우리의 세로 길이(1 <= N <= 100000)
N = int(input())

# dp[i] : 사자를 최대 i마리까지 넎는 경우의 수
dp = [0] * (N+1)
dp[0] = 1 # 사자 0마리 넣는 경우의 수
dp[1] = 3

if N >= 2:
    for i in range(2, N+1):
        dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901
print(dp[N])