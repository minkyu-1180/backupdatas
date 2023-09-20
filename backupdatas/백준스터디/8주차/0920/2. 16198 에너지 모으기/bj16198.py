# 백준 16198. 에너지 모으기
import sys
sys.stdin = open("bj16198input.txt")

def backtracking(arr, N, c):
    global result

    if N == 2:
        if result < c:
            result = c
        return

    for i in range(1, N-1):
        arr1 = arr[0:i]
        arr2 = arr[i+1:N]
        new_arr = arr1 + arr2
        backtracking(new_arr, N-1, c+(arr[i-1] * arr[i+1]))

T = int(input())
for tc in range(T):
    N = int(input()) # 에너지 구슬의 개수(3 <= N <= 10)
    arr = list(map(int, input().split())) # 에너지 구슬의 무게
    result = 0
    backtracking(arr, N, 0)
    print(result)