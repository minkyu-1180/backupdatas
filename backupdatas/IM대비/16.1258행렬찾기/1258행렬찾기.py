# IM 대비 16. 행렬찾기
import sys
sys.stdin = open("행렬찾기input.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    subsets = [] # 부분집합의 행-열을 담을 리스트
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                sub = [1, 1, 0] # 부분집합 행 / 열 / 크기
                y = i
                x = j
                while x + 1 < N and arr[i][x+1]:
                    x += 1
                sub[1] = x - j + 1
                while y + 1 < N and arr[y+1][j]:
                    y += 1
                sub[0] = y - i + 1
                sub[2] = (x-j+1) * (y-i+1)

                # 이미 확보한 부분집합은 다시 순회하지 않도록 0으로 초기화
                for row in range(i, y+1):
                    for col in range(j, x+1):
                        arr[row][col] = 0
                # 부분집합의 row, col, size 정보 담아두기
                subsets.append(sub)


    # 선택정렬(앞에서부터 출력되어야 하는 순으로 정렬하기)
    min_idx = 0
    for i in range(len(subsets)-1):
        min_idx = i
        for j in range(i+1, len(subsets)):
            if subsets[min_idx][2] > subsets[j][2]:
                min_idx = j
            elif subsets[min_idx][2] == subsets[j][2]:
                if subsets[min_idx][0] > subsets[j][0]:
                    min_idx = j
        subsets[min_idx], subsets[i] = subsets[i], subsets[min_idx]

    print(f'#{test_case} {len(subsets)}', end = ' ')
    for row, col, size in subsets:
        print(row, end = ' ')
        print(col, end = ' ')
    print()


