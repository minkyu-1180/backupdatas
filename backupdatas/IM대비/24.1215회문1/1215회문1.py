# IM 대비 24. 회문1
import sys
sys.stdin = open("회문1input.txt")

for test_case in range(1, 11):
    K = int(input()) # 회문의 글자수
    arr = [list(input()) for _ in range(8)]

    result = 0
    # 1. 열 별로 찾기
    for i in range(8):
        for j in range(9-K):
            ispalin = [arr[i][j+l] for l in range(K)]
            if ispalin == ispalin[::-1]: # 뒤집어도 같을 경우
                result += 1
    # 2. 행 별로 찾기
    for j in range(8):
        for i in range(9-K):
            ispalin = [arr[i+l][j] for l in range(K)]
            if ispalin == ispalin[::-1]:
                result += 1
    print(f'#{test_case} {result}')

