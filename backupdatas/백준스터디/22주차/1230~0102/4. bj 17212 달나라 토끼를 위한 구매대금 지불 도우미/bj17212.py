# 백준 17212. 달나라 토끼 어쩌구~
import sys
sys.stdin = open("bj17212input.txt")

dp = [i for i in range(100001)]

for i in range(2, 100001):
    if i - 2 >= 0:
        dp[i] = min(dp[i], dp[i-2]+1)
    if i - 5 >= 0:
        dp[i] = min(dp[i], dp[i-5]+1)
    if i - 7 >= 0:
        dp[i] = min(dp[i], dp[i-7] + 1)
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 달나라 토끼가 지불해야 하는 금액(0 <= N <= 100000)
    N = int(input())
    '''
    동전 종류 : 1, 2, 5, 7
    동전 개수가 최소가 되도록 해야 합법
    1 1 1 3 
    '''
    print(dp[N])