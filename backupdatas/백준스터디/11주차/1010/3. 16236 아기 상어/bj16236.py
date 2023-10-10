# 백준 16236. 아기상어
import sys
sys.stdin = open("bj16236input.txt")
from collections import deque
def is_root(y, x, i, j, shark_size):
    que = deque([])
    que.append((y, x))
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    while que:
        y, x = que.popleft()
        if y == i and x == j:
            return True
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                if arr[ny][nx] <= shark_size:
                    visited[ny][nx] = 1
                    que.append((ny, nx))
    return False




T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    shark_pos = (0, 0)
    fishes = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] == 9:
                shark_pos = (i, j)
                lst[j] = 0
            elif lst[j]:
                fishes.append((i, j, lst[j]))
        arr.append(lst)
    # print(arr)
    result = 0
    shark_size = 2
    c = 0
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while fishes:
        y, x = shark_pos
        min_dist = int(1e9)
        min_idx = -1
        for k in range(len(fishes)):
            i, j, fish_size = fishes[k]
            if shark_size <= fish_size:
                continue
            if shark_size > fish_size:
                # 더 큰 경우 -> 갈수 있는 루트가 있으면 비교
                dist = abs(i - y) + abs(j - x)
                if min_dist > dist and is_root(y, x, i, j, shark_size):
                    min_dist = dist
                    min_idx = k
        if min_idx == -1:
            break

        ny, nx, size = fishes[min_idx]
        fishes = fishes[:min_idx] + fishes[min_idx+1:]
        shark_pos = (ny, nx)
        result += min_dist
        if c + 1 == shark_size:
            shark_size += 1
            c = 0

    print(result)
