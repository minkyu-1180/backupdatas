# 백준 10826 피보나치수4
import sys
sys.stdin = open("10826input.txt")
N = int(input())

if N < 2:
    print(N)
else:
    x, y = 0, 1
    for _ in range(2, N+1):
        x, y = y, x+y
    print(y)
