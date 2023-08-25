# IM 대비 8. 백준 2578 빙고
import sys
sys.stdin = open("2578빙고input.txt")

arr = [list(map(int, input().split())) for _ in range(5)]

vs_arr = []
for _ in range(5):
    nums = list(map(int, input().split()))
    vs_arr += nums

result = 0
bingo = 0
for num in vs_arr:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 0
                result += 1

                # 1. 본인 기준 행
                row_bingo = 0
                for x in range(5):
                    if arr[i][x] == 0:
                        row_bingo += 1
                if row_bingo == 5:
                    bingo += 1

                # 본인 기준 열
                col_bingo = 0
                for y in range(5):
                    if arr[y][j] == 0:
                        col_bingo += 1
                if col_bingo == 5:
                    bingo += 1

                # 본인 기준 pos_diag
                if i == j:
                    pos_diag_bingo = 0
                    for idx in range(5):
                        if arr[idx][idx] == 0:
                            pos_diag_bingo += 1
                    if pos_diag_bingo == 5:
                        bingo += 1
                if i + j == 4:
                    neg_diag_bingo = 0
                    for idx in range(5):
                        if arr[idx][4-idx] == 0:
                            neg_diag_bingo += 1
                    if neg_diag_bingo == 5:
                        bingo += 1
    if bingo >= 3:
        break
print(result)