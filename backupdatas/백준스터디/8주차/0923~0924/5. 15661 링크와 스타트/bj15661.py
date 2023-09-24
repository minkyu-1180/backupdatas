# 백준 15661. 링크와 스타트
import sys
sys.stdin = open("bj15661input.txt")

def backtracking(c):
    global result

    if c == N:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += arr[i][j] + arr[j][i]
                if visited[i] == 0 and visited[j] == 0:
                    link += arr[i][j] + arr[j][i]

        if result > abs(start-link):
            result = abs(start-link)

        return

    visited[c] = 1
    backtracking(c+1)
    visited[c] = 0
    backtracking(c+1)



T = int(input())
for tc in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = int(1e9)
    backtracking(0)
    print(result)