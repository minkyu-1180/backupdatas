# 백준 11052. 카드 구매하기
import sys
sys.stdin = open("bj11052input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 민규가 구매하려고 하는 카드 개수(1 <= N <= 1000)
    N = int(input())
    # P1 ~ Pn
    arr = list(map(int, input().split()))
    '''
    카드 i개를 살 때 가장 비싸게 사는게 목표
    
    '''
    # dp[i] : 카드 i개 살 때 가장 비싸게 살 수 있는 금액
    dp = [0] + arr[:]
    for i in range(2, N+1):
        for j in range(1, i):
            dp[i] = max(dp[i], dp[i-j]+arr[j-1])
    print(dp)