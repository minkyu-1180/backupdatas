# 백준 7562. 나이트의 이동
import sys
sys.stdin = open("7562input.txt")

def bfs(y1, x1, y2, x2):
    if y1 == y2 and x1 == x2:
        return 0
    dir = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, -2], [2, -1], [1, 2], [2, 1]]
    queue = [[y1, x1]]

    visited = [[0] * L for _ in range(L)]
    visited[y1][x1] = 1
    while queue:
        i, j = queue.pop(0)

        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if ni == y2 and nj == x2:
                    break
                queue.append([ni, nj])
    return visited[y2][x2] - 1



T = int(input())
for tc in range(T):
    L = int(input()) # 체스판 한 변의 길이(4 <= L <= 300)
    y1, x1 = list(map(int, input().split())) # 현재 나이트의 칸
    y2, x2 = list(map(int, input().split())) # 이동할 나이트의 칸


    result = bfs(y1, x1, y2, x2)
    print(result)