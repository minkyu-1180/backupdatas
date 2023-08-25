# IM 대비 13. Ladder1
import sys
sys.stdin = open("Ladder1input.txt")

for test_case in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    i = 99
    for k in range(100):
        if arr[99][k] == 2:
            j = k

    while i != 0:
        # 오른쪽이 1이면 오른쪽에 0이 나올때까지 이동
        if 0 <= j + 1 <= 99 and arr[i][j+1]:
            while j + 1 <= 99 and arr[i][j+1]:
                j += 1

        # 왼쪽이 1이면 왼쪽에 0이 나올때까지 이동
        elif 0 <= j - 1 <= 99 and arr[i][j-1]:
            while 0 <= j - 1 and arr[i][j-1]:
                j -= 1

        # 위의 조건문에서 나온 경우 row_idx 한칸 올려주기
        # 무한루프 방지, 조건문에 안 걸리는 경우는 무조건 위로
        i -= 1
    print(f'#{test_case} {j}')

