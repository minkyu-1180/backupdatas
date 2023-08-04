# sw 문제해결 기본 2일차 - Sum
from pprint import pprint as pp
import sys
sys.stdin = open("suminput.txt")
for test_case in range(1, 11):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # i번째 행 / i번째 열 / 대각선 들의 요소들의 합을 넣어줄 리스트
    row_sum = [0] * 100
    col_sum = [0] * 100
    diag_sum = [0] * 2

    # 각 row의 합 구하기
    for i in range(100):
        for j in range(100):
            row_sum[i] += arr[i][j]
    row_max = 0
    for i in range(100):
        if row_max < row_sum[i]:
            row_max = row_sum[i]

    # 각 col의 합 구하기
    for j in range(100):
        for i in range(100):
            col_sum[j] += arr[i][j]
    col_max = 0
    for i in range(100):
        if col_max < col_sum[i]:
            col_max = col_sum[i]

    diag_max = 0
    for i in range(100):
        diag_sum[0] += arr[i][i]
        diag_sum[1] += arr[i][99-i]
    if diag_sum[0] >= diag_sum[1]:
        diag_max = diag_sum[0]
    else:
        diag_max = diag_sum[1]

    result = 0
    result_lst = [row_max, col_max, diag_max]
    for ele in result_lst:
        if result < ele:
            result = ele
    print(f'#{test_case} {result}')


