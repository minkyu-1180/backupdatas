# IM 대비 21. 농작물 수확하기
import sys
sys.stdin = open("농작물input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    middle = N // 2

    result = 0
    if N == 1:
        result = arr[0][0]
    else:
        # 0 ~ (middle-1) & (middle+1) ~ (N-1)
        for i in range(middle):
            for j in range(middle-i, middle+i+1):
                result += arr[i][j]
                result += arr[N-1-i][j]

        # middle번 row
        for j in range(N):
            result += arr[middle][j]

    print(f'#{test_case} {result}')

