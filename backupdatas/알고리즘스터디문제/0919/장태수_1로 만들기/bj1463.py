# 백준 1463. 1로 만들기
import sys
sys.stdin = open("bj1463input.txt")
N = int(input())
# DP 사용 
# dp[i] : i를 1로 만드는 데 드는 최소 횟수
dp = [0] * (N+1)
# dp[1] = 1(1을 1로 만드는 데 드는 최소횟수 = 1)
for i in range(2, N+1):
    # i가 1로 가는 데 필요한 일반적인 연산 
    dp[i] = 1 + dp[i-1]

    # 2로 나누어 떨어질 경우, 기존 dp값과 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나누어 떨어질 경우, 기존 dp값과 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])