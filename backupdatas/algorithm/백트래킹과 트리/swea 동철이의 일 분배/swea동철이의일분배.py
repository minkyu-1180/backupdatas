# swea 동철이의 일 분배
import sys
sys.stdin = open("swea동철이의일분배input.txt")

def backtracking(i, percentage):
    global result
    if i == N+1:
        if result < percentage:
            result = percentage

    if result < percentage:
        for j in range(1, N+1):
            if visited[j] == 0:
                visited[j] = i
                backtracking(i+1, percentage * (arr[i][j]/100))
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
    result = 0
    percentage = 100
    backtracking(1, percentage)

    print(f'#{tc} {result:.6f}')