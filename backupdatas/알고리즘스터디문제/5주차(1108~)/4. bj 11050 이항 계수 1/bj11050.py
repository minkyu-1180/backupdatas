# 백준 11050. 이항 계수 1
import sys
from itertools import combinations
sys.stdin = open("bj11050input.txt")

def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N-1)

N, K = map(int, input().split())
print(factorial(N)//(factorial(N-K) * factorial(K)))