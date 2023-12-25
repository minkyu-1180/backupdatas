# 백준 15988. 1, 2, 3 더하기 - 3
import sys
sys.stdin = open("bj15988input.txt")

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4

'''
dp[n] : n을 1, 2, 3의 합으로 나타내는 방법
- n-1을 나타내는 방법 + 1
- n-2를 나타내는 방법 + 2
- n-3을 나타내는 방법 + 3
dp[4]
- 1 1 1 1
- 1 2 1
- 2 1 1
- 3 1

- 1 1 2
- 2 2

- 1 3 

'''
for n in range(4, 1000001):
    dp[n] = (dp[n - 1] + dp[n - 2] + dp[n - 3]) % 1000000009

T = int(input())
for tc in range(T):
    N = int(input())

    print(dp[N])