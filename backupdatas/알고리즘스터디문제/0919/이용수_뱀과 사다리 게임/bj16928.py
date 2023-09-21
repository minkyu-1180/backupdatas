# 백준 16928. 뱀과 사다리 게임
from collections import deque
import sys
sys.stdin = open("bj16928input.txt")

def bfs():
    while que:
        i, j, c = que.popleft()
        now = arr[i][j]
        for x in dice:
            if x + now < 100:
                next = x + now
                # 해당 값이 처음으로 99가 되면 return
                if next == 99:
                    return c+1

                # 아직 방문 X
                if visited[next // 10][next % 10] == 0:
                    # 추가로 이동해야 할 경우
                    if ladder_snake[next // 10][next % 10] != (-1, -1):
                        ni, nj = ladder_snake[next // 10][next % 10][0], ladder_snake[next // 10][next % 10][1]
                    else:
                        ni, nj = next // 10, next % 10

                    visited[ni][nj] = visited[i][j] + 1
                    que.append((ni, nj, c + 1))


N, M = map(int, input().split())
arr = [[10 * i] * 10 for i in range(10)]
for i in range(10):
    lst = arr[i]
    for j in range(10):
        lst[j] += j

dice = list(range(1, 7))

# [i][j]에서 어디로 이동하게 되는지에 대한 정보
# 뱀과 사다리가 없는 경우, (-1, -1)이 입력되어있음
ladder_snake = [[(-1, -1)] * 10 for _ in range(10)]
for _ in range(N+M):
    start, end = map(int, input().split())
    start_i = (start-1) // 10
    start_j = (start-1) % 10
    end_i = (end-1) // 10
    end_j = (end-1) % 10
    ladder_snake[start_i][start_j] = (end_i, end_j)

# for i in range(10):
#     print(ladder_snake[i])
que = deque()
# i, j, c : i번 row, j번 col 방문 : c
que.append((0, 0, 0)) # 시작점
# now = arr[0][0]
visited = [[0] * 10 for _ in range(10)]
result = 0
visited[0][0] = 1
result = bfs()
print(result)





