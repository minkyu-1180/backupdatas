# sw academy - 1210. Ladder1
from pprint import pprint as pp
import sys
sys.stdin = open("ladderinput.txt")

for test_case in range(1, 11):
    T = int(input())
    N = 100

    arr = [list(map(int, input().split())) for _ in range(N)]
    end = 0
    for j in range(N):
        if arr[N-1][j] == 2:
            end = j

    i = N-2
    while i > 0:
        # end가 왼쪽 벽
        if end == 0:
            # 오른쪽 값이 1일 경우 -> 오른쪽으로 이동, 위로는 X
            if arr[i][end+1] == 1:
                arr[i][end] = 0
                end += 1
            # 양쪽 다 갈 수 없을 경우 -> 위로 이동
            else:
                i -= 1
        elif end == N-1:
            if arr[i][end-1] == 1:
                arr[i][end] = 0
                end -= 1
            else:
                i -= 1
        # 양쪽 다 뜷려있을 경우
        else:
            if arr[i][end - 1] == 1:
                arr[i][end] = 0
                end -= 1
            elif arr[i][end + 1] == 1:
                arr[i][end] = 0
                end += 1
            # 양쪽 다 0
            else:
                i -= 1
    print(f'#{test_case} {end}')
