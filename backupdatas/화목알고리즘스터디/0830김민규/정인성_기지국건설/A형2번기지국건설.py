# 정인성님 - 기지국 건설
from collections import deque

T = int(input())

# 열이 홀수 / 짝수일 때 방향
odd_d = [[-1, 0], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] # 12시, 9시, 3시, 7시, 6시, 5시
even_d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0]] # 11시 12시 1시 9시 3시 6시

for test_case in range(1, T+1):
    N, M = map(int, input().split()) # 열 / 행 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 기지국 별 사용자 정보
    result = 0
    # (i, j) 기준 bfs 실행
    for i in range(N):
        for j in range(M):
            que1 = deque([])
            que1.append([i, j])
            que2 = deque([])
            que2.append([arr[i][j]])
            while que1:
                now = que1.popleft()
                sums = que2.popleft()
                ni, nj = now[0], now[1]
                if ni % 2:  # 홀수
                    dir = odd_d
                else:
                    dir = even_d

                for di, dj in dir:
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < M:
                        que1.append([[ni, nj]] + now)
                        if len(sums)
                        que2.append([arr[i][j]] + sums)






