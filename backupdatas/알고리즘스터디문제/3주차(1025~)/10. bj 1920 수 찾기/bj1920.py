# 백준 1920. 수 찾기
import sys
sys.stdin = open("bj1920input.txt")

N = int(input())
arr_N = list(map(int, input().split()))
arr_N.sort()
M = int(input())
arr_M = list(map(int, input().split()))
for num in arr_M:
    s = 0
    e = N-1
    while s <= e:
        mid = (s+e)//2
        if num == arr_N[mid]:
            print(1)
            break
        if num > arr_N[mid]:
            s = mid+1
        elif num < arr_N[mid]:
            e = mid-1
    if s > e:
        print(0)