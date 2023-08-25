# IM 대비 11. 색칠하기
import sys
sys.stdin = open("색칠하기input.txt")


bosaek = {1 : 2,
          2 : 1}
def purple(i_1, j_1, i_2, j_2, color):
    # 해당 범위 내에서 생성되는 보라색의 개수
    # 중복으로 생성되는 보라색은 제외(첫 보라 개수)
    p = 0
    for i in range(i_1, i_2 + 1):
        for j in range(j_1, j_2 + 1):
            # 아직 색이 칠해지지 않은 경우
            if arr[i][j] == 0:
                arr[i][j] = color
            # 다른 색이 칠해진 경우 -> 보라색
            elif arr[i][j] == bosaek[color]:
                arr[i][j] = 3
                p += 1
    return p




T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N개의 색칠 영역(2 <= N <= 30)
    arr = [[0] * 10 for _ in range(10)]
    result = 0
    for _ in range(N):
        i_1, j_1, i_2, j_2, color = map(int, input().split())
        result += purple(i_1, j_1, i_2, j_2, color)

    print(f'#{test_case} {result}')
