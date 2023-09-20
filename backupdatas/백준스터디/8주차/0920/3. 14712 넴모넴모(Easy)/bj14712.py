# 백준 14712. 넴모넴모(Easy)
import sys
sys.stdin = open("bj14712input.txt")

def backtracking(c):
    global result

    if c >= N * M:
        result += 1
        return
    # 현재 놓을지 말지 결정할 row, col idx
    i = c//M
    j = c%M
    if i >= 1 and j >= 1:
        # 만약 위쪽을 보았을 때 i, j에 1을 넣으면 넴모 2X2가 되는 경우
        if [[arr[i-1][j-1], arr[i-1][j]], [arr[i][j-1], arr[i][j]]] == [[1, 1], [1, 0]]:
            backtracking(c+1)
        else:
            arr[i][j] = 1
            backtracking(c+1)
            arr[i][j] = 0
            backtracking(c+1)
    else:
        arr[i][j] = 1
        backtracking(c+1)
        arr[i][j] = 0
        backtracking(c+1)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    result = 0
    backtracking(0)
    print(result)
