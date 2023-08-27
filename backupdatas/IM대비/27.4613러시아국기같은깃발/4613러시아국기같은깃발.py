# IM 대비 27. 러시아 국기같은 깃발
import sys
sys.stdin = open("러시아input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = N * M

    # W로 바꿀 끝 줄 / B로 바꿀 끝 줄 설정
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            # 긱 줄 별로 흰/파/빨로 바꾸는 개수
            w_c = 0
            for y in range(i+1):
                for x in range(M):
                    if arr[y][x] != 'W':
                        w_c += 1
            b_c = 0
            for y in range(i+1, j+1):
                for x in range(M):
                    if arr[y][x] != 'B':
                        b_c += 1
            r_c = 0
            for y in range(j+1, N):
                for x in range(M):
                    if arr[y][x] != 'R':
                        r_c += 1
            if result > w_c + b_c + r_c:
                result = w_c + b_c + r_c
    print(f'#{test_case} {result}')