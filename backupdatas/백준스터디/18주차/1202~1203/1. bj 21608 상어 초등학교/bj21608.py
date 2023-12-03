# 백준 21608. 상어 초등학교

import sys
sys.stdin = open("bj21608input.txt")


# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸이 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
def select(std):
    max_c1 = -1
    max_c2 = -1
    selected = [0, 0]
    # 이후 조건 3 만족 위해 거꾸로
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            # 우선 비어있는 칸인지 확인
            if arr[i][j] == 0:
                # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸이 가장 많은 칸으로 자리를 정한다.
                c1 = 0
                c2 = 0
                for di, dj in dir:
                    ni = i + di
                    nj = j + dj
                    if 0 < ni <= N and 0 < nj <= N:
                        # 비어있는 경우
                        if arr[ni][nj] == 0:
                            c2 += 1
                        elif arr[ni][nj] in like[std]:
                            c1 += 1
                # 조건 1 만족 선행
                if max_c1 < c1:
                    selected = [i, j]
                    max_c1 = c1
                    max_c2 = c2
                # 조건1 같은 것이 여러개 -> 조건 2 만족 선생
                elif max_c1 == c1:
                    if max_c2 <= c2:
                        selected = [i, j]
                        max_c2 = c2
    return selected


# 원래 T는 없음
# T = int(input())
# for tc in range(T):
# N : 학생 수의 루트(3 <= N <= 20)
# 학생 번호 : 1 ~ N**2
N = int(input())

# 교실의 가장 왼쪽 윗 칸 : (1, 1)
# 교실의 가장 오른쪽 아랫 칸 : (N, N)
arr = [[0] * (N+1) for _ in range(N+1)]

# like[i] : i가 좋아하는 학생들의 번호
like = [set() for _ in range(N**2 + 1)]
# (r1, c1)과 (r2, c2)가 인접 === abs(r1-r2) + abs(c1-c2) = 1
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(N**2):
    lst = list(map(int, input().split()))
    std = lst[0]
    for k in range(1, 5):
        like[std].add(lst[k])
    i, j = select(std)
    arr[i][j] = std

result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        c = 0
        std = arr[i][j]
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 < ni <= N and 0 < nj <= N:
                is_friend = arr[ni][nj]
                if is_friend in like[std]:
                    c += 1
        # 1명 -> 1점 ~ 4명 = 1000점
        if c > 0:
            result += 10 ** (c-1)
print(result)
    # for _ in range(N**2):
    #     # std : 학생 번호
    #     # ni : std가 좋아하는 학생 번호(ni != nj if i != j)
    #     # 자기 자신을 좋아하는 학생은 X
    #     std, n1, n2, n3, n4 = map(int, input().split())
    #     '''
    #     1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸이 가장 많은 칸으로 자리를 정한다.
    #     2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    #     3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    #     -> 첫 학생은 (1+N)//2, (1+N//2)
    #     '''
    #     # wts : 앉을 칸 후보
    #     wts = []
    #     for i in range(1, N**2+1):


