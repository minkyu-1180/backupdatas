# 백준 2110. 공유기 설치
import sys
sys.stdin = open("bj2110input.txt")

# N : 집의 개수(2 <= N <= 200000)
# C : 공유기 개수(2 <= C <= N)
N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
# 목표 : 가장 인접한 두 공유기 사이의 거리의 최대값 구하기
min_dist = 1 # 최소거리
max_dist = arr[N-1]-arr[0] # 최대 거리(양 끝에 설치할 경우가 최대 케이스)
result = 0 # 결과값
while min_dist <= max_dist:
    mid = (min_dist+max_dist)//2
    # 현재 설치된 공유기 개수
    c = 1
    last_idx = 0 # 가장 앞쪽에 설치
    for i in range(1, N):
        # 가장 최근에 설치된 위치로부터의 거리가 >= mid -> 하나 설치(최소가 mid가 되어아 해서 하나만)
        if arr[i]-arr[last_idx] >= mid:
            c += 1
            # 최근 설치된 위치 갱신
            last_idx = i
    # 더 많이 설치됨 -> 최소거리 증가(수를 줄여야 해서) 및 갱신
    if c >= C:
        min_dist = mid+1
        result = mid
    # 더 적게 설치됨 -> 최대거리 감소(수를 늘려야 해서)
    else:
        max_dist = mid-1
print(result)


