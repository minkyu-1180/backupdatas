# A형 2번
import sys
sys.stdin = open("a형2번input.txt")

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split()) # 주어지는 기지국들의 행/열 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 기지국별 유저 수

    odd_d = [[-1, 0], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] # i가 odd일 때의 방향
    even_d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0]] # i가 even일 때의 방향
    result1 = 0 # 기지국 4개 최대 비용을 담을 변수
    result1_idx = []
    result2 = 0
    result2_idx = []
    # 각 요소 별로 연결되는 4개의 기지국 유저 합의 제곱중 최대값을 구한 후,
    # 해당 최대값을 기존 최대값과 비교
    for i in range(N):
        for j in range(M):

            # 1. bfs
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            queue = [[[i, j]]]

            while queue:
                now = queue.pop(0)
                ni, nj = now[0][0], now[0][1]

                # if visited[ni][nj] > 4:
                    # break

                if ni%2: # 현재 행이 odd인 경우
                    dir = odd_d
                else: # 현재 행이 even인 경우
                    dir = even_d

                # 1. 본인 기준 쭉쭉 뻗어나가기
                for di, dj in dir:
                    if 0 <= ni + di < N and 0 <= nj + dj < M and visited[ni+di][nj+dj] == 0:
                        visited[ni+di][nj+dj] = visited[ni][nj] + 1
                        new = [[ni+di, nj+dj]] + now
                        if len(new) == 4:
                            # print(new, end = ' ')
                            c = 0
                            for y, x in new:
                                c += arr[y][x]
                            if result1 < c:
                                result1 = c
                                result1_idx = new
                        else:
                            queue.append(new)
                            ni += di
                            nj += dj

    for i in range(N):
        for j in range(M):
            # 2. 1 - 3구조
            if i%2: # 홀수인 경우
                dir = odd_d
            else:
                dir = even_d

            c = arr[i][j]
            adjs = []
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    adjs.append(arr[ni][nj])
            adjs.sort(reverse = True)
            if len(adjs) >= 3:
                for k in range(3):
                    c += adjs[k]
                if result2 < c:
                    result2 = c
                    result2_idx = new
    print(result1, result2)
    print(result1_idx, result2_idx)





