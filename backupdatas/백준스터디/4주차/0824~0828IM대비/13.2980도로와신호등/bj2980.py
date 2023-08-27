# IM 대비 13. 백준 2980 도로와 신호등
import sys
sys.stdin = open("2980도로와신호등input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N 신호등 수(1 <= N <= 100)
    # L : 도로 길이(1 <= L <= 1000)
    N, L = map(int, input().split())

    # 원소 : [D, R, G] - 신호등 위치 / 빨간불 유지 / 파란불 유지
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 각 arr의 위치까지 접근하는 방법
    t = 0 # 지나간 시간
    d = 0 # 현재 위치


    # 더이상 신호등을 만나지 않을 경우 종료
    while arr:
        # 가장 가까운 신호등 정보
        sinho = arr[0]
        t += 1
        # 신호등을 만나지 않은 경우/더이상 마주칠 신호등이 없을 경우
        if d < sinho[0]:
            d += 1

        else:
            r, g = sinho[1], sinho[2]
            if 0 < t % (r + g) <= r: # 빨간불
                continue
            else:
                d += 1
                arr.pop(0)
        # 도착
        if d == L:
            break
    t += (L-d) # 시간이 곧 남은 거리
    print(t)

