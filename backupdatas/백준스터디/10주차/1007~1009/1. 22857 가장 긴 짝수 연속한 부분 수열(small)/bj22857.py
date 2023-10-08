# 백준 22857
import sys
sys.stdin = open("bj22857input.txt")

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    arr[i] %= 2

result = 0
for i in range(1, N+1):
    for j in range(K+1):
        if arr[i] == 0:  # 짝수일 때
            dp[i][j] = dp[i-1][j] + 1
        elif j > 0:  # 홀수일 때
            dp[i][j] = dp[i-1][j-1]
        if j == K and result < dp[i][j]:
            result = dp[i][j]

print(result)