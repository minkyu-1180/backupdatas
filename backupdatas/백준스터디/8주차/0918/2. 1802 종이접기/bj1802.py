# 백준 1802. 종이접기
import sys
sys.stdin = open("bj1802input.txt")
T = int(input())
for tc in range(T):
    arr = list(map(int, input()))

    end = len(arr)
    result = 'YES'
    flag = True
    while 0 < end:
        middle = (end) // 2
        for i in range(middle):
            if arr[i] + arr[end-1-i] != 1:
                flag = False
                break

        if not flag:
            result = 'NO'
            break

        end = middle


    print(result)