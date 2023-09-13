# 백준 11501. 주식
import sys
sys.stdin = open("bj11501input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    max_v = 0
    max_idx = -1
    while max_idx < N:
        start = max_idx + 1
        if start == N:
            break

        for i in range(start, N):
            if max_v <= arr[i]:
                max_v = arr[i]
                max_idx = i

        if start != max_idx:
            for i in range(start, max_idx):
                result -= arr[i]
            result += (max_idx - start) * arr[max_idx]
        max_v = 0
    print(result)