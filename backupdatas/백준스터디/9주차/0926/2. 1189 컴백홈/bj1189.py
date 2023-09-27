# 백준 1189. 컴백홈
import sys
sys.stdin = open("bj1189input.txt")

def backtracking(c, i, j):
    global result
    if c == K:
        if i == 0 and j == C-1:
            result += 1
        return

    for di, dj in dir:
        ni = i + di
        nj = j + dj
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0 and arr[ni][nj] == '.':
            visited[ni][nj] = 1
            backtracking(c+1, ni, nj)
            visited[ni][nj] = 0
'''
R :  (1 <= R <= 5)
C :  (1 <= C <= 5)
K :  (1 <= K <= R x C)
'''
R, C, K = map(int, input().split())

arr = [list(input()) for _ in range(R)]
start = (R-1, 0)
end = (0, C-1)
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0] * C for _ in range(R)]
visited[R-1][0] = 1

result = 0
backtracking(1, R-1, 0)
print(result)

