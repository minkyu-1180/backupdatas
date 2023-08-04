# sw academy - 11092. 최대 최소의 간격

import sys
sys.stdin = open("minmaxdiffinput.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr= list(map(int, input().split()))

    max = 0
    max_idx = 0
    for i in range(N):
        if max <= arr[i]:
            max = arr[i]
            max_idx = i

    min = 10
    min_idx = N-1
    for i in range(N-1, -1, -1):
        if min >= arr[i]:
            min = arr[i]
            min_idx = i

    if max_idx >= min_idx:
        result = max_idx - min_idx
    else:
        result = min_idx - max_idx
    print(f'#{test_case} {result}')