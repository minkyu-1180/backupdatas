# sw academy 4843. 특별한 정렬

import sys
sys.stdin = open("specialsortinput.txt")


def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = SelectionSort(arr)
    result_arr = [0] * N
    middle = N // 2

    # N이 짝수일 때
    if N % 2 == 0:
        for i in range(middle):
            result_arr[2 * i] = sorted_arr[N-1 - i]
            result_arr[2 * i + 1] = sorted_arr[i]

    # N이 홀수일 때
    if N % 2 == 1:
        for i in range(middle+1):
            result_arr[2 * i] = sorted_arr[N - 1 - i]
            result_arr[2 * i + 1] = sorted_arr[i]
    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(result_arr[i], end = ' ')
    print()

