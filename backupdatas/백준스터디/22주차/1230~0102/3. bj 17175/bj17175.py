# 백준 17175. 피보나치는 지겨웡~
import sys
sys.stdin = open("bj17175input.txt")

# def fibonacci(N):
#     global c
#     c += 1
#     c %= 1000000007
#     if N < 2:
#         return N
#         # return N
#
#     return fibonacci(N-2) + fibonacci(N-1)
dp = [0] * 51
dp[0] = dp[1] = 1
for i in range(2, 51):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007


# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 피보나치 함수에 인자로 입력할 값(0 <= N <= 50)
    N = int(input())
    print(dp[N])
