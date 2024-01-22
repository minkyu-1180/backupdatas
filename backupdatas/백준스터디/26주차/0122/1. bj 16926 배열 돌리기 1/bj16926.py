# 백준 16926. 배열 돌리기 1
import sys
sys.stdin = open("bj16926input.txt")

def change(y, x):
    global now
    last = arr[y][x]
    arr[y][x] = now
    now = last
    return

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N, M : 주어지는 배열 크기
    # R : 수행해야 하는 회전 수
    N, M, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(R):
        # 현재 i 기준으로 4방향 change 진행
        for i in range(min(N, M)//2):
            y, x = i, i
            # 각 i별로 시작 위치 잡기
            now = arr[y][x]
            # 1. 왼쪽으로 이어가기
            for j in range(i+1, N-i):
                y = j
                change(y, x)
            # 2. 아래쪽으로 이어가기
            for j in range(i+1, M-i):
                x = j
                change(y, x)

            # 3. 오른쪽으로 이어가기
            for j in range(i+1, N-i):
                y = N-j-1
                change(y, x)

            # 4. 위쪽으로 이어가기
            for j in range(i+1, M-i):
                x = M-j-1
                change(y, x)

    for i in range(N):
        for j in range(M):
            print(arr[i][j], end=' ')
        print()