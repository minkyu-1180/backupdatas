# 백준 18870. 좌표 압축
import sys
sys.stdin = open("bj18870input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 좌표의 개수(1 <= N <= 1000000)
    N = int(input())
    # N개의 좌표
    arr = list(map(int, input().split()))
    short_arr = list(set(arr))
    short_arr.sort()
    dictionary = dict()
    for i in range(len(short_arr)):
        num = short_arr[i]
        dictionary[num] = i

    result = [0] * N
    for i in range(N):
        num = arr[i]
        result[i] = dictionary[num]
    print(*result)
