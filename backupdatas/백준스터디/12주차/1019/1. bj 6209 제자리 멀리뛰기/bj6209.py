# 백준 6209. 제자리 멀리뛰기
import sys
sys.stdin = open("bj6209input.txt")

# D : 돌섬으로부터 탈출구까지의 거리(1 <= D <= 1000000000)
# N : 작은 돌섬의 수(0 <= N <= 50000)
# M : 제거할 수 있는 작은 돌섬의 수(0 <= M <= N)
D, N, M = map(int, input().split())
if N == 0: # 작은 돌섬 X -> 갇힌 섬에서 탈출구로 한 번에 뛰어야 함
    print(D)
else:
    arr = [0]
    for _ in range(N):
        arr.append(int(input()))
    # 갇힌 돌섬으로부터의 거리를 오름차순으로 정렬
    arr.sort()
    arr.append(D)

    min_dist = 0
    max_dist = arr[-1]
    while min_dist <= max_dist:
        # mid : 현재 상황에서 이 거리보다는 더 뛸거임 한번에
        mid = (min_dist + max_dist)//2
        counts = 0 # 몇 개 치움?
        # position = 0 # 가장 최근에 제거한 돌과 시작점 사이 거리
        i = 0
        for j in range(i+1, N+1):
            # 현재 상황에서 도착점까지 거리가 mid보다 작음 --> 오류 -> 그냥 다 업새버리기

            if D - arr[j] < mid:
                counts += (N+1) - j
                break

            # 더 작은 거리 -> 치워버리기(counts 증가)
            if arr[j] - arr[i] < mid:
                counts += 1
            # 더 큰 거리 -> position, i 갱신
            else:
                i = j
        # print(counts)
        # 최소 dist가 mid일 때, 돌을 없애는 횟수가 M보다 클 경우
        # -> 최소 dist를 줄임으로써, 돌을 덜 없앨 수 있게
        if counts > M:
            max_dist = mid-1
        # 최소 dist가 mid일 때, 돌을 없애는 횟수가 M보다 작을 경우
        # -> 최소 dist를 늘림으로써, 돌을 더 없앨 수 있게
        else:
            min_dist = mid+1
    print(max_dist)



