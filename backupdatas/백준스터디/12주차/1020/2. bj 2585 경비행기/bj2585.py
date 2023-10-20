# 백준 2582. 경비행기
import sys
sys.stdin = open("bj2585input.txt")

# input = sys.stdin.readline

# N : 출발지와 목적지를 제외한 비행장의 수 (3 <= N <= 1000)
# K : 최대 경유 횟수
N, K = map(int, input().split())
S = [0, 0]
T = [10000, 10000]

y_larger = []
x_larger = []
xy_same = []

min_dist = 10000 * (2**0.5) # 최대 연료통 용량
max_dist = 0
for _ in range(N):
    y, x = map(int, input().split())
    max_dist += (y**2 + x**2)*(2**0.5)
    if y > x:
        y_larger.append([y, x])
    elif x < y:
        x_larger.append([y, x])
    else:
        xy_same.append([y, x])

min_l = min_dist//10 + 1
max_l = max_dist//10 + N
# 최대 허용 중간급유 횟수가 0일 경우, 출발지 -> 도착지 직행 밖에 불가능
if K == 0:
    print(min_l)
else:
    y_larger.sort()
    x_larger.sort()
    xy_same.sort()
    # 가운데로 가로지르는 경로 존재 시 무조건 그 경로로 가는게 제일 빠름
    if xy_same:
        y, x = xy_same[-1]
        pass
    else:
        while min_l <= max_l:
            mid = (min_l + max_l)//2

