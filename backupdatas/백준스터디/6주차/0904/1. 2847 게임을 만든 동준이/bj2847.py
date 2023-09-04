# 백준 2847. 게임을 만든 동준이
import sys
sys.stdin = open("bj2847input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))

    result = 0
    for i in range(N-1, 0, -1):
        if arr[i] <= arr[i-1]:
            result += arr[i-1] - arr[i] + 1
            arr[i-1] = arr[i] - 1

    print(result)

