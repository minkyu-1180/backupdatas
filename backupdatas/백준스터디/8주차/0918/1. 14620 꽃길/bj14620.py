# 백준 14620. 꽃길
from collections import deque
import sys
sys.stdin = open("bj14620input.txt")


N = int(input()) # 화단 한 변의 길이(6 <= N <= 10)
# 화단의 지점당 가격(각 가격 : 0 ~ 200)
arr = [list(map(int, input().split())) for _ in range(N)]
result = 7500
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i1 in range(1, N-1):
    for j1 in range(1, N-1):
        idx_1 = (i1, j1)

        for i2 in range(1, N-1):
            for j2 in range(1, N-1):
                if abs(i1 - i2) + abs(j1 - j2) > 2:
                    idx_2 = (i2, j2)

                    for i3 in range(1, N-1):
                        for j3 in range(1, N-1):
                            if (abs(i1 - i3) + abs(j1 - j3) > 2) and (abs(i2 - i3) + abs(j2 - j3) > 2):
                                idx_3 = (i3, j3)
                                sum_three = arr[i1][j1] + arr[i2][j2] + arr[i3][j3]
                                for di, dj in dir:
                                    ni1, nj1 = i1 + di, j1 + dj
                                    ni2, nj2 = i2 + di, j2 + dj
                                    ni3, nj3 = i3 + di, j3 + dj
                                    sum_three += arr[ni1][nj1] + arr[ni2][nj2] + arr[ni3][nj3]

                                if result > sum_three:
                                    result = sum_three


print(result)