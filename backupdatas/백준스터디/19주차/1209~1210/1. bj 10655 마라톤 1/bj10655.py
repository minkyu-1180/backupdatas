# 백준 10655. 마라톤 1
import sys
sys.stdin = open("bj10655input.txt")

# i : 현재 승원이가 있는 위치
# dist : 승원이가 i번 체크포인트까지 오는데 걸린 거리
# flag : 승원이가 앞서서 건너뛴 적이 있는지 체크
def backtracking(i, dist, flag):
    global result

    # N번 체크포인트까지 도착
    if i == N:
        if result > dist:
            result = dist
        return

    now_i, now_j = arr[i]
    next_i, next_j = arr[i+1]

    plus = abs(next_i - now_i) + abs(next_j - now_j)
    # 이미 앞에서 건너뛰기 실행 -> i+1
    if flag:
        backtracking(i+1, dist + plus, flag)
    else:
        next2_i, next2_j = arr[i + 2]
        plus2 = abs(next2_i - now_i) + abs(next2_j - now_j)
        if i == N-2:
            backtracking(i+2, dist + plus2, not flag)
        else:
            # 아직 건너뛰기 안하려면
            backtracking(i+1, dist + plus, flag)
            # 건너뛰기 하려면
            backtracking(i+2, dist + plus2, not flag)


# N : 체크포인트의 수(3 <= N <= 100000)
N = int(input())

arr = []
for i in range(N):
    # x, y : 체크포인트 i의 x, y좌표(-1000 <= x, y <= 1000)
    # 박승원 : 1번, N번 체크포인트를 제외한 다른 체크포인트 중 하나 건너뛸거임
    # 체크포인트는 순서대로 방문
    x, y = map(int, input().split())
    arr.append((x, y))

dists1 = [] # dists1[i] : i번 ~ i+1번 사이 거리
dists2 = [] # dists2[i] : i번 ~ i+2번 사이 거리
result = 0
for i in range(N-1):
    p1 = arr[i]
    p2 = arr[i+1]
    dist1 = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    result += dist1
    dists1.append(dist1)
    if i < N-2:
        p3 = arr[i+2]
        dist2 = abs(p3[0] - p1[0]) + abs(p3[1] - p1[1])
        dists2.append(dist2)
# print(arr)
# print(dists1)
# print(dists2)

max_v = 0
for i in range(N-2):
    dist1_1 = dists1[i]
    dist1_2 = dists1[i+1]

    dist2 = dists2[i]
    if max_v < dist1_1 + dist1_2 - dist2:
        max_v = dist1_1 + dist1_2 - dist2

result -= max_v
print(result)