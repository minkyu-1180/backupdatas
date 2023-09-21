# 백준 22233. 가희와 키워드
import sys
sys.stdin = open("bj22233input.txt")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    memo = dict()
    for _ in range(N):
        memo[input()] = 0

    result = N
    for _ in range(M):
        lst = list(input().split(","))
        for s in lst:
            if s in memo.keys() and memo[s] == 0:
                memo[s] = 1
                result -= 1
        print(result)

