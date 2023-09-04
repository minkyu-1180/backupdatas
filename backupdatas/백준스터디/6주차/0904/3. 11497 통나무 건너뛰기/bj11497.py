# 백준 11497. 통나무 건너뛰기
import sys
sys.stdin = open("bj11497input.txt")


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort() # 정렬
    result = [0] * (N+1)
    result[0] = result[N] = arr[0]

    for i in range(1, N):
        if i%2:
            result[N-1 - i//2] = arr[i]
        else:
            result[i//2] = arr[i]

    max_v = 0
    for i in range(0, N):
        if max_v < abs(result[i] - result[i+1]):
            max_v = abs(result[i] - result[i+1])
    print(max_v)



