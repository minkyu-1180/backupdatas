# sw academy 4837. 부분집합의 합

import sys
sys.stdin = open("sumsub2input.txt")


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    result = 0
    subsets = []
    for i in range(1 << 12):
        subset = []

        for j in range(12):
            if i & (1 << j):
                subset.append(arr[j])

        if len(subset) == N:
            subsets.append(subset)


    for sub in subsets:
        subsum = 0
        for ele in sub:
            subsum += ele
        if subsum == K:
            result += 1
    print(f'#{test_case} {result}')

