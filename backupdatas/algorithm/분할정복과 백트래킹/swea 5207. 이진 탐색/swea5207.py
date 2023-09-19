# swea 5207
import sys
sys.stdin = open("swea5207input.txt")

def BinarySearch(arr, key, l, r):
    global result, flag
    if l > r:
        return
    m = (l+r)//2
    if arr[m] == key:
        result += 1

    elif arr[m] > key:
        if flag == 'start' or flag == 'right':
            flag = 'left'
            BinarySearch(arr, key, l, m-1)
    elif arr[m] < key:
        if flag == 'start' or flag == 'left':
            flag = 'right'
            BinarySearch(arr, key, m+1, r)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    arr = sorted(arr_A)

    result = 0
    for key in arr_B:
        flag = 'start'
        BinarySearch(arr, key, 0, N-1)
    print(f'#{tc} {result}')
