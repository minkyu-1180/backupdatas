# 백준 1041. 주사위
import sys
sys.stdin = open("bj1041input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    if N == 1:
        arr.sort()
        for i in range(5):
            result += arr[i]
    else:
        min_val = []
        for i in range(3):
            min_val.append(min(arr[i], arr[5-i]))
        min_val.sort()
        one_min = min_val[0]
        two_min = min_val[0] + min_val[1]
        three_min = sum(min_val)

        result = one_min * ((N-2)*(N-2) + 4*(N-1)*(N-2)) + two_min * (4*(N-2) + 4*(N-1)) + three_min * 4
    print(result)