# 백준 3190. 뱀
import sys
from collections import deque
sys.stdin = open("bj3190input.txt")

# i, j : 시작 머리 위치
def bfs(i, j):
    result = 0
    # 시작 dir : 동쪽
    d = 0
    # 시작 위치 정해주기
    arr[i][j] = 1
    que = deque()
    que.append((i, j))

    while que:
        result += 1
        di, dj = dir[d]
        ni = i + di
        nj = j + dj

        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 1:
            return result

        # 사과 발견 -> 크기 늘어남
        if arr[ni][nj] == 2:
            # 사과 위치가 본인 위치가 됨(한 칸 크기 증가)
            arr[ni][nj] = 1
            que.append((ni, nj))
            # 만약 방향을 돌려야 하는 상황 -> 돌려주기
            if result in dictionary.keys():
                C = dictionary[result]
                if C == 'L':
                    d = (d - 1) % 4
                else:
                    d = (d + 1) % 4
        # 그냥 빈칸 -> 크기 안늘고 전체적으로 앞으로 당겨짐(꼬리부분 삭제되고 머리부분 추가)
        elif arr[ni][nj] == 0:
            arr[ni][nj] = 1
            que.append((ni, nj))
            tail_i, tail_j = que.popleft()
            arr[tail_i][tail_j] = 0

            if result in dictionary.keys():
                C = dictionary[result]
                if C == 'L':
                    d = (d - 1) % 4
                else:
                    d = (d + 1) % 4
        i, j = ni, nj
    return result

T = int(input())
for tc in range(T):
    # N : 보드의 크기(2 <= N <= 100)
    N = int(input())
    # K : 사과 개수(0 <= K <= 100)
    K = int(input())

    # arr : 보드 정보
    arr = [[0] * N for _ in range(N)]

    # 사과 위치 정보(2)
    for _ in range(K):
        i, j = map(int, input().split())
        arr[i-1][j-1] = 2
    # L : 방향 전환 정보 주어지는 횟수(1 <= L <= 100)
    # 배열로 하면 너무 커보임(10000개까지;)
    dictionary = dict()
    L = int(input())
    for _ in range(L):
        # 뱀의 방향 변환 정보(X초 뒤 C로 방향 회전)
        X, C = input().split()
        X = int(X)
        dictionary[X] = C

    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    '''
    뱀은 몸길이를 늘려 머리를 다음칸에 위치
    벽이나 자기자신의 몸과 부딪히면 게임 끝
    이동한 칸에 사과가 있을 경우, 해당 칸의 사과가 없어지고 꼬리는 움직이지 않음(몸길이 변화 + 1)
    이동한 칸에 사과가 없으면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌(몸길이 변화 X)
    '''
    print(bfs(0, 0))


