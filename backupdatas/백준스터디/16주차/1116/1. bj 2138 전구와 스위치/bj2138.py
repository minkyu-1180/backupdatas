# 백준 2138. 전구와 스위치
import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("bj2138input.txt")

def greedy(now_arr, end_arr, c):
    global result

    if c >= result:
        return

    if now_arr == end_arr:
        if result > c:
            result = c
        return
    copied_arr = deepcopy(now_arr)

    for i in range(N):
        if i == 0:
            pass
        else:
            pass


# N : 스위치와 전구의 개수 (2 <= N <= 100000)
# 1번 ~ N번 스위치/전구
N = int(input())

# 현재 전구들의 상태
start_arr = list(input())

# 최종 전구의 상태
end_arr = list(input())

result = int(1e9)