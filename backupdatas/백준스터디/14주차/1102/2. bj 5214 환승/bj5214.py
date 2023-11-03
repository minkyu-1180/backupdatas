# 백준 5214. 환승
import sys
from collections import deque
sys.stdin = open("bj5214input.txt")

def bfs():
    visited = [0] * (N+1)
    visited[1] = 1
    que = deque()
    que.append((1, 1))


# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 역의 수(1 <= N <= 100000)
    # K : 한 하이퍼튜브가 서로 연결하는 역의 개수(1 <= K <= 1000)
    # M : 하이퍼튜브의 개수(1 <= M <= 1000)
    N, K, M = map(int, input().split())

    tubes = []
    for _ in range(M):
        tube = list(map(int, input().split()))
        tubes.append(set(tube))

