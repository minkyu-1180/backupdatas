# 백준 6593. 상범 빌딩
import sys
sys.stdin = open("bj6593input.txt")
from collections import deque

def bfs(start, end):
    que = deque()
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    l_s, r_s, c_s, cnt = start
    que.append(start)
    visited[l_s][r_s][c_s] = 0

    while que:
        now = que.popleft()
        l, r, c, cnt = now
        # 도착지인 경우, 도착하는데 걸린 시간(분) return
        if (l, r, c) == end:
            return cnt
        for dl, dr, dc in dir:
            nl = l + dl
            nr = r + dr
            nc = c + dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                # 방문하지 않은 위치 중 갈 수 있는 곳이면 방문 처리 후 큐에 삽입
                if arr[nl][nr][nc] != '#' and visited[nl][nr][nc] == -1:
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    que.append((nl, nr, nc, cnt+1))
    # 도착 실패한 경우, 0 return
    return 0
# 같은 층에서 동서남북
dir_same = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
# 다른 층으로 상하좌우
dir_updown = [[-1, 0, 0], [1, 0, 0]]
dir = dir_same + dir_updown
# print(dir)

# L : 상범 빌딩의 층 수(1 <= L <= 30)
# R : 상범 빌딩의 한 층의 행(1 <= R <= 30)
# C : 상범 빌딩의 한 층의 열(1 <= C <= 30)
L, R, C = map(int, input().split())

'''
상범 빌딩 : 각 변의 길이가 1인 정유견체로 이루어짐
- 금으로 이루어진 경우 : 지나갈 수 없음(#)
- 비어있는 경우 : 지나갈 수 잇음(.)
- 시작 : S
- 끝 : E

이동방법(1분 소요)
- 동서남북 : 동일 층에서 
- 상하 : 층 이동
'''

while True:
    if L == 0:
        break
    arr = []
    start = ()
    end = ()
    # 각 층별로 행과 열 모양 파악
    for l in range(L):
        l_list = []
        for r in range(R):
            r_list = list(input())
            l_list.append(r_list)
            for c in range(C):
                string = r_list[c]
                if string == 'S':
                    start = (l, r, c, 0)
                elif string == 'E':
                    end = (l, r, c)
        arr.append(l_list)
        black = input()
    # print(arr)
    # print(start)
    # print(end)
    # print(bfs(start, end))
    result = bfs(start, end)
    if result:
        print(f'Escaped in {result} minute(s).')
    else:
        print('Trapped!')

    L, R, C = map(int, input().split())
