# 백준 1699. 제곱수의 합
import sys
sys.stdin = open("bj1699input.txt")

# dp[i] : 1 + 1 + 1 + ....가 최대값 -> 갱신해봅시당
dp = [i for i in range(100001)]
dp[0] = 0
for i in range(1, 100001):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # 100000의 루트 : 316.22776601683796
    # N : 주어진 수(1 <= N <= 100000)
    N = int(input())
    # print(100000**0.5)
    print(dp[N])