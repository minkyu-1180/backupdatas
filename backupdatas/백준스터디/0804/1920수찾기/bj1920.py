# 1920. 수 찾기

import sys
sys.stdin = open("1920input.txt")

# 주어지는 정수의 개수 N과 N개의 주어진 정수를 담은 리스트
N = int(input())
n_arr = list(map(int, input().split()))
# 주어지는 찾아야 하는 정수의 개수 M과 M개의 찾을 정수를 담은 리스트
M = int(input())
m_arr = list(map(int, input().split()))

# 정렬
n_arr = sorted(n_arr)


# 이진검색 함수 정의
def BinarySearch(arr, wtf):
    l = 0
    r = len(arr) - 1
    while l <= r:
        middle = (l + r)//2
        if arr[middle] == wtf:
            return 1
        elif arr[middle] > wtf:
            r = middle - 1
        elif arr[middle] < wtf:
            l = middle + 1
    return 0


# 각 index에 대해 함수 호출(찾으면 1, 못찾으면 0)
for i in range(M):
    print(BinarySearch(n_arr, m_arr[i]))