# 백준 2485. 가로수
import sys
sys.stdin = open("bj2485input.txt")
from math import gcd
# 원래 T는 없음
T = int(input())
for tc in range(T):
    N = int(input())

    result = 0
    min_gcd = 0
    arr = []
    for i in range(N):
        arr.append(int(input()))
        if i >= 2:
            if i == 2:
                min_gcd = gcd(arr[1]-arr[0], arr[2]-arr[1])
            else:
                min_gcd = gcd(min_gcd, arr[i]-arr[i-1])
    for i in range(1, N):
        result += (arr[i]-arr[i-1])//min_gcd - 1
    print(result)

    # print(arr)
    # print(dist)
