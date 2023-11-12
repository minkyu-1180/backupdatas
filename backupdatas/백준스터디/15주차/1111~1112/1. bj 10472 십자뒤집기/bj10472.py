# 백준 10472. 십자뒤집기
import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("bj10472input.txt")

def change(i, j, my_arr, c):
    copy_arr = deepcopy(my_arr)
    # i, j : 클릭한 점 위치
    # my_arr : 현재 que에서 받아온 배열
    # copy_arr : 복사본 -> 복사본에 변화 -> visited 여부 확인
    for di, dj in dir:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            if copy_arr[ni][nj] == 0:
                copy_arr[ni][nj] = 1
            else:
                copy_arr[ni][nj] = 0
    my_str = ''
    for i in range(3):
        for j in range(3):
            my_str += str(copy_arr[i][j])
    # bit 연산으로 바꾸기
    my_num = int(my_str, 2)
    if visited[my_num]==0:
        visited[my_num] = 1
        return (copy_arr, c+1)
    else:
        return (-1, -1)

def bfs():
    visited[0] = 1
    que = deque()
    # 시작 arr, count 삽입
    que.append((start_arr, 0))

    while que:
        # 현재 진행된 arr 형태, now_arr가 되기까지 클릭 횟수
        now_arr, c = que.popleft()
        if now_arr == arr:
            return c
        # 현재 arr에 대해, 특정 칸을 클릭 시 bit연산 변화 후 visited 확인
        for i in range(3):
            for j in range(3):
                return_val = change(i, j, now_arr, c)
                if return_val == (-1, -1):
                    continue
                que.append(return_val)



# P : 테스트 케이스 숫자(0 <= P <= 50)
P = int(input())
for p in range(P):
    # arr[i][j] = * : 검은색
    # arr[i][j] = . : 흰색
    arr = []
    for i in range(3):
        lst = input()
        start = []
        for l in lst:
            # 검 -> 1
            if l == '*':
                start.append(1)
            elif l == '.':
                start.append(0)
        arr.append(start)
    # print(arr)
    dir = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
    # 목표 : 모든 칸이 흰색인 3X3 보드를 입력으로 주어지는 보드의 형태로 바꾸기
    # 한 칸 클릭 -> 해당 칸과 인접한 동서남북 네 칸의 색 변화
    start_arr = [[0] * 3 for _ in range(3)]
    # 어차피 3 * 3이니까, 현재 진행되는 arr의 모습을 que에 담아버리자
    # visited 처리는 어떻게? . 2**9 = 512
    # 이거 예전에 bit연산으로 바꾸는거 했었는디
    # bfs에 초기 start_arr 넣어주고, 000000000 == 0이니까 visited[0] = 1처리해주고
    visited = [0] * 512
    result = bfs()
    print(result)