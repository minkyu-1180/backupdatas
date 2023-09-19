# swea 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open("swea격자판의숫자이어붙이기input.txt")

def backtracking(i, j, string):
    global result

    if len(string) == 7:
        cases.add(string)
        result += 1
        return

    for di, dj in dir:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            if len(string) != 6 or string + arr[ni][nj] not in cases:
                backtracking(ni, nj, string + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cases = set()
    result = 0
    for i in range(4):
        for j in range(4):
            backtracking(i, j, arr[i][j])

    print(f'#{tc} {result}')