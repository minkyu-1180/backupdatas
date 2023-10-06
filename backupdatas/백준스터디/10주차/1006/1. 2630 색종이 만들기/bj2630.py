# 백준 2630. 색종이 만들기
import sys
sys.stdin = open("bj2630input.txt")

def divide_conquer(i, j, N):
    global white, blue

    if N == 1:
        if arr[i][j] == 1:
            blue += 1
        else:
            white += 1
        return

    flag1 = arr[i][j]
    flag2 = True
    for y in range(i, i+N):
        for x in range(j, j+N):
            if arr[y][x] != flag1:
                flag2 = False
                break
        if not flag2:
            break
    if not flag2:
        N //= 2
        divide_conquer(i, j, N)
        divide_conquer(i, j + N, N)
        divide_conquer(i + N, j, N)
        divide_conquer(i + N, j + N, N)
    else:
        if flag1:
            blue += 1
        else:
            white += 1
        return


N = int(input()) # 2, 4, 8, 16, 32, 128 중 하나
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0
print()
divide_conquer(0, 0, N)
print(white)
print(blue)