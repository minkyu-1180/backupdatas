# 백준 2775 부녀회장이 될테야
import sys
sys.stdin = open("2775input.txt")

T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    n = int(input())
    arr = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            arr[i] += arr[i-1]
    print(arr[-1])

