import sys
# input = sys.stdin.readline
from copy import deepcopy
sys.stdin = open("bj15683input.txt")

# c : 현재 설정한 cctv 개수
# arr : 현재 설정한 cctv들을 적용한 방들의 상태
def backtracking(c, arr):
    global result
    # 모든 cctv 방향을 다 설정해준 경우
    if c == cctv_num:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
        if result > cnt:
            result = cnt
        return

    # 현재 상황의 arr 복사(backtracking에 영향 안주려고)
    copied = deepcopy(arr)

    i, j, type = cctv_arr[c]

    for cctv_d in cctv_dir[str(type)]:
        for d in cctv_d:
            ni, nj = i, j
            while True:
                # 같은 방향으로 쭉쭉 나아가기
                ni += dir[d][0]
                nj += dir[d][1]
                # 종료조건 : 범위 벗어난 경우
                if 0 > ni or ni >= N or 0 > nj or nj >= M:
                    break
                # 종료조건 : 벽을 만난 경우
                if copied[ni][nj] == 6:
                    break

                # 갈수 있는데 아직 안간 길이면 1로 만들기
                elif copied[ni][nj] == 0:
                    copied[ni][nj] = 1
        backtracking(c + 1, copied)
        copied = deepcopy(arr)

N, M = map(int, input().split())
arr = []
cctv_arr = []
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(M):
        cctv = lst[j]
        if 1 <= cctv <= 5:
            # CCTV 좌표 및 종류 저장
            cctv_arr.append((i, j, cctv))
cctv_num = len(cctv_arr)
# 상 하 좌 우
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# cctv 번호에 따른 방향 설정 방법
cctv_dir = {
    '1' : [[0], [1], [2], [3]],
    '2' : [[0, 1], [2, 3]],
    '3' : [[0, 2], [0, 3], [1, 2], [1, 3]],
    '4' : [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    '5' : [[0, 1, 2, 3]],

}

result = int(1e9)
backtracking(0, arr)
print(result)