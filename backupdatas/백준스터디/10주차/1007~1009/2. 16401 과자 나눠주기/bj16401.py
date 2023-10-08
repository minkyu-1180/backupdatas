# 백준 16401. 과자 나눠주기
import sys
sys.stdin = open("bj16401input.txt")

T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    arr = list(map(int, input().split()))

    s = 1
    e = max(arr)
    while s <= e:
        mid = (s+e)//2
        c = 0
        for i in range(N):
            c += arr[i]//mid
            if c >= M:
                s = mid+1
                break
        else:
            e = mid-1
    print(e)


