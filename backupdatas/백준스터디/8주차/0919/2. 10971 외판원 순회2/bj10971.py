# 백준 10971. 외판원 순회 2
import sys
sys.stdin = open("bj10971input.txt")

def backtracking(now, c, cost):
    global result

    if cost >= result:
        return

    if c == N:
        # 마지막 방문한 것에서 start로 되돌아오는 비용 추가
        if arr[now][i]:
            cost = cost + arr[now][i]
            if result > cost:
                result = cost
        return

    for next in range(N):
        if visited[next] == 0 and arr[now][next]:
            visited[next] = 1
            backtracking(next, c+1, cost + arr[now][next])
            visited[next] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 1000000 * (N+1)
for i in range(N):
    visited = [0] * N
    visited[i] = 1
    backtracking(i, 1, 0)
print(result)