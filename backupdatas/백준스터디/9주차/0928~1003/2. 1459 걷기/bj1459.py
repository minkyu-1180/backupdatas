# 백준 1459. 걷기
import sys
from collections import deque
sys.stdin = open("bj1459input.txt")

def backtracking(y, x, c):

    que = deque()


T = int(input())
for tc in range(T):
    # (X, Y) : 집의 위치
    # W : 한 블록 가는데 걸리는 시간
    # S : 대각선으로 한 블록을 가로지르는 시간
    X, Y, W, S = map(int, input().split())
    dist_1 = W * (X+Y)
    if (X+Y)%2:
        dist_2 = (max(X, Y) - 1) * S + W
    else:
        dist_2 = max(X, Y) * S
    dist_3 = (min(X, Y) * S) + (abs(X-Y) * W)
    result = min(dist_1, dist_2, dist_3)
    print(result)
