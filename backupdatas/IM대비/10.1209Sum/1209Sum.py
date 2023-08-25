# IM 대비 10. Sum
import sys
sys.stdin = open("Suminput.txt")
for test_case in range(1, 11):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    row_m = col_m = diag_m = 0 # 최대값 초기화


    # 1. row 최대합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if row_m < row_sum:
            row_m = row_sum

    # 2. col 최대합
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if col_m < col_sum:
            col_m = col_sum

    # 3. diagonal 최대합
    diag_sum = 0
    reverse_diag_sum = 0
    for i in range(100):
        diag_sum += arr[i][i]
        reverse_diag_sum += arr[i][99-i]
    if diag_sum > reverse_diag_sum:
        diag_m = diag_sum
    else:
        diag_m = reverse_diag_sum

    # row, col, diag 중 최대값
    result = max(row_m, col_m, diag_m)

    print(f'#{test_case} {result}')

