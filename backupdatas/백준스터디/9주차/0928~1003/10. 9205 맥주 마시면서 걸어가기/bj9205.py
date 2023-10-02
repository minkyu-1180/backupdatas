# 백준 9205. 맥주 마시면서 걸어가기
import sys
sys.stdin = open("bj9205input.txt")
from collections import deque

def bfs():
    while que:
        i, j = que.popleft()
        if arr[-1] == [i, j]:
            return "happy"

        for idx in range(len(arr)):
            ni, nj = arr[idx]
            if i != ni or j != nj:
                dist = abs(i - ni) + abs(j - nj)
                if visited[idx] == 0 and dist <= 1000:
                    visited[idx] = 1
                    que.append([ni, nj])


    return "sad"



T = int(input())
for tc in range(T):
    N = int(input())

    arr = []
    for _ in range(N+2):
        y, x = map(int, input().split())
        arr.append([y, x])

    que = deque()
    que.append(arr[0])
    visited = [0] * (N+2)
    visited[0] = 1
    print(bfs())
