# swea 5209. 최소 생산 비용
import sys
sys.stdin = open("swea5209input.txt")


def backtracking(i, cost):
    global result
    if i == N+1:
        if result > cost:
            result = cost

    if result > cost:
        for j in range(1, N+1):
            if visited[j] == 0:
                visited[j] = i
                backtracking(i+1, cost + arr[i][j])
                visited[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 1 <= N <= 16

    # arr[i][j] : i번 사람이 j번 일을 성공할 확률(단위 : 퍼센트)
    arr = [[0] * N]
    for _ in range(N):
        lst = [0] + list(map(int, input().split()))
        arr.append(lst)
    # visited[j] : i == j번 일을 i한테 맡김김
    visited = [0] * (N+1)
    result = 100 * N
    cost = 0
    backtracking(1, cost)

    print(f'#{tc} {result}')