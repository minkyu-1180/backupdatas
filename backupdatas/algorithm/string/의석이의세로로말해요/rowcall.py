# 의석이의 세로로 말해요
import sys
sys.stdin = open("rowcallinput.txt")
T = int(input())
for test_case in range(1, T+1):
    arr = [input() for _ in range(5)]

    # 최대 열 길이
    max_col = 0
    for string in arr:
        c = 0
        for s in string:
            c += 1
        if max_col < c:
            max_col = c
    # 모든 행의 길이 맞춰주기(빈 곳 : !로 채우기)
    for i in range(len(arr)):
        ith_row_len = len(arr[i])
        for j in range(ith_row_len+1, max_col+1):
            arr[i] += '!'
    # !인 곳을 빼고 연결
    result = ''
    for j in range(max_col):
        for i in range(5):
            if arr[i][j] != '!':
                result += arr[i][j]
    print(f'#{test_case} {result}')


