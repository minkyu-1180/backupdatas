# 회문 1
import sys
sys.stdin = open("reversesame1input.txt")

for test_case in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    row_c = 0
    for i in range(8):
        string = arr[i]
        for j in range(8-N+1):
            new_str = ''
            reverse_str = ''
            for k in range(j, j+N):
                new_str += string[k]
                reverse_str += string[2 * j + N - 1 - k]
            if new_str == reverse_str:
                row_c += 1

    col_c = 0
    for j in range(8):
        for i in range(8-N+1):
            new_str = ''
            reverse_str = ''
            for k in range(i, i+N):
                new_str += arr[k][j]
                reverse_str += arr[2 * i + N - 1 - k][j]
            if new_str == reverse_str:
                col_c += 1
    result = row_c + col_c
    print(f'#{test_case} {result}')