# swea 5205. 퀵 정렬
import sys
sys.stdin = open("swea5205input.txt")

def partition(arr, l, r):
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def QuickSort(arr, l, r):
    if l < r:
        m = partition(arr, l, r)
        QuickSort(arr, l, m-1)
        QuickSort(arr, m+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 정수 개수
    arr = list(map(int, input().split())) # 정렬 전 리스트

    QuickSort(arr, 0, N-1)
    result = arr[N//2]
    print(f'#{tc} {result}')