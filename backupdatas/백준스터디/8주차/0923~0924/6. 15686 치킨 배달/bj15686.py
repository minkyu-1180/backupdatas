# 백준 15686. 치킨 배달
import sys
sys.stdin = open("bj15686input.txt")

def chicken_dist():
    global result
    dist_sum = 0
    for i, j in home:
        dist = int(1e9)
        for k in range(len(visited)):
            if visited[k] == 1:
                y, x = chicken[k]
                if dist > abs(i-y) + abs(j-x):
                    dist = abs(i-y) + abs(j-x)
        dist_sum += dist
    if result > dist_sum:
        result = dist_sum


def backtracking(c, idx):

    # 다 채웠거나 끝까지 다 본 경우(c <= M 상태)
    if c == M or idx == len(visited):
        chicken_dist()
        return

    for i in range(idx, len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(c+1, i+1)
            visited[i] = 0


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home = []
    chicken = []
    result = int(1e9)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))
            elif arr[i][j] == 2:
                chicken.append((i, j))
    visited = [0] * len(chicken)
    backtracking(0, 0)
    print(result)