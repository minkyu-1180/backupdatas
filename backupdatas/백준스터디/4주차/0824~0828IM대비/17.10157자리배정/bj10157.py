# IM 대비 17. 백준 10157 자리배정
import sys
sys.stdin = open("10157자리배정input.txt")


def seat(K):
    if K > M * N:  # 배열의 범위를 벗어남
        return 0
    arr = [[0] * (M + 1) for _ in range(N + 1)]
    arr[1][1] = 1

    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    d = 0
    i = j = 1
    num = 2
    while num <= K:
        ni = i + dir[d][0]
        nj = j + dir[d][1]
        if N >= ni >= 1 and M >= nj >= 1 and arr[ni][nj] == 0:
            i = ni
            j = nj  # 현재 위치 갱신
            arr[i][j] = num
            if num == K:
                break
            num += 1
        else:
            d = (d + 1) % 4  # 방향전환

    return j, i


T = int(input())
for test_case in range(1, T+1):
    M, N = map(int, input().split())
    K = int(input())
    result = seat(K)
    if result:
        print(*result)
    else:
        print(result)

