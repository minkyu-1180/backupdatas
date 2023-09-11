# 백준 21921. 블로그
import sys
sys.stdin = open("bj21921input.txt")

T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))

    if max(arr) == 0:
        print("SAD")
    else:
        max_v = sum(arr[0:X])
        max_c = 1

        sum_v = sum(arr[0:X])
        for i in range(X, N):
            sum_v += (arr[i] - arr[i-X])
            if max_v < sum_v:
                max_v = sum_v
                max_c = 1
            elif max_v == sum_v:
                max_c += 1

        print(max_v)
        print(max_c)
