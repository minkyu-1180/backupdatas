# A형 2번
import sys
sys.stdin = open("a형2번input.txt")

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split()) # 주어지는 기지국들의 행/열 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 기지국별 유저 수

    odd_d = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [1, 1]] # i가 odd일 때의 방향
    even_d = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1]]  # i가 even일 때의 방향

    result1 = 0 # 기지국 4개 최대 비용을 담을 변수
    # 각 요소 별로 연결되는 4개의 기지국 유저 합의 제곱중 최대값을 구한 후,
    # 해당 최대값을 기존 최대값과 비교
    for i in range(N):
        for j in range(M):

            # 1. bfs
            queue = [[[i, j]]]

            while queue:
                now = queue.pop(0) # 지금까지 걸어온 자취인덱스들을 담아놓은 리스트
                ni, nj = now[0][0], now[0][1] # 가장 앞의 인덱스 = 가장 최근에 간 인덱스 -> 접근

                # if visited[ni][nj] > 4:
                    # break

                if nj%2: # 현재 행이 odd인 경우
                    dir = odd_d
                else: # 현재 행이 even인 경우
                    dir = even_d

                # 1. 본인 기준 쭉쭉 뻗어나가기
                for di, dj in dir:
                    # 새로운 인접 인덱스가 지금 길을 따라오는동안 방문한 적이 있는가?
                    if 0 <= ni + di < N and 0 <= nj + dj < M and [ni+di, nj+dj] not in now:
                        # 방문한 적이 없을 경우 방문 가능 -> 새롭게 방문한 노드를 현재까지 방문한 노드모음에 추가
                        new = [[ni+di, nj+dj]] + now
                        # 네 개의 기지국 건설된 시점 -> 최대값과 비교
                        if len(new) == 4:
                            # print(new, end = ' ')
                            c = 0
                            for y, x in new:
                                c += arr[y][x]
                            if result1 < c:
                                result1 = c
                                result1_idx = new
                        # 아직 네 개의 기지국 건설 X -> 큐에 추가
                        else:
                            queue.append(new)

    result2 = 0
    for i in range(N):
        for j in range(M):
            # 2. 1 - 3구조
            if j%2: # 홀수인 경우
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
                    result2_idx = adjs[:4]
    result = max(result1, result2)
    print(result**2)






