# 백준 2294. 동전 2
import sys
from collections import defaultdict
sys.stdin = open("bj2294input.txt")

# N : 동전 종류(1 <= N <= 100)
# K : 동전의 가치 합 목표(1 <= K <= 10000)
N, K = map(int, input().split())
# 동전 종류
coins = set()
for _ in range(N):
    coin = int(input())
    # 동전의 가치가 K보다 작거나 같을 경우면 추가(아니면 필요 X)
    # 도대체 왜 동전 가치가 <= 100000으로 준거지
    # 같은 동전이 여러번 주어질수도 있음
    if coin <= K:
        coins.add(coin)
# print(coins)
coins = sorted(list(coins))
# print(coins)

# dp[i] : 가치의 합이 K원이 되는 최소 개수
# dp[i] : 동전의 가치 종류coin이 있을 경우, dp[i-coin] + 1
dp = [int(1e9)] * 10001
dp[0] = 0
min_coin = coins[0]
# 만약 가장 작은 값이 K보다 클 경우, 못만든다
if min_coin > K:
    print(-1)
else:
    '''
    [1, 5, 12], 15
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3]
    [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 1, 2, 3, 3]
    '''


    # 가치가 낮은 코인부터 채우기
    for coin in coins:
        for i in range(coin, K+1):
            dp[i] = min(dp[i], dp[i-coin]+1)

    if dp[K] < int(1e9):
        print(dp[K])
    else:
        print(-1)
