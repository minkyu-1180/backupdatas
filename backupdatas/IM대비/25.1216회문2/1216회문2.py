# Ik 대비 25. 회문2
import sys
sys.stdin = open("회문2input.txt")

def row_palin(k, arr):
    for i in range(100):
        for j in range(101-k):
            for l in range(k//2):
                if arr[i][j+l] != arr[i][j+k-1-l]:
                    break
            else:
                return True

def col_palin(k, arr):
    for j in range(100):
        for i in range(101-k):
            for l in range(k//2):
                if arr[i+l][j] != arr[i+k-1-l][j]:
                    break
            else:
                return True


for test_case in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    for k in range(100, -1, -1):
        if row_palin(k, arr) or col_palin(k, arr):
            print(f'#{test_case} {k}')
            break
