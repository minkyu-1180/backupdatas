# 백준 9461 파도반 수열
import sys
sys.stdin = open("9461input.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    P = [0] + [1] * 3 + [2] * 2 + [0] * (N-5)
    for i in range(6, N+1):
        P[i] = P[i-1] + P[i-5]

    print(P[N])