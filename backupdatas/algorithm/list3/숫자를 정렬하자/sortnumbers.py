# sw academy 1966. 숫자를 정렬하자

import sys
sys.stdin = open("sortnumbersinput.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f'#{test_case}', end = ' ')
    for ele in arr:
        print(ele, end = ' ')
    print()