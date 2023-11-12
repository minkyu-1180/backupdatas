# 백준 10872. 팩토리얼
import sys
sys.stdin = open("bj10872input.txt")

def factorial(N):
    if N == 1:
        return N

    return N * factorial(N-1)

# 원래 T는 없음
T = int(input())
for tc in range(T):
    N = int(input())
    if N == 0:
        print(1)
    else:
        print(factorial(N))