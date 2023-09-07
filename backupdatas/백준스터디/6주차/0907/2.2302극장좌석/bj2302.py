# 백준 2302. 극장 좌석
import sys
sys.stdin = open("bj2302input.txt")

N = int(input())
M = int(input())
arr = [0] + list(range(1, N+1))
vip_list = []
for _ in range(M):
    vip = int(input())
    vip_list.append(vip)

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    if i in vip_list or (i-1) in vip_list:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N])

