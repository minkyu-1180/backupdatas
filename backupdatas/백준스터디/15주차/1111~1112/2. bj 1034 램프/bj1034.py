# 백준 1034. 램프
import sys
from copy import deepcopy
sys.stdin = open("bj1034input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 행의 개수(1 <= N <= 50)
    # M : 열의 개수(1 <= M <= 50)
    N, M = map(int, input().split())
    # arr : N X M의 램프의 상태
    # arr[i][j] = 0 : (i, j)의 램프는 꺼져있음
    # arr[i][j] = 1 : (i, j)의 램프는 켜져있음
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            arr[i][j] = int(arr[i][j])

    # K : 스위치를 누르는 횟수(0 <= K <= 1000)
    K = int(input())

    # i번 행이 켜져 있다 === i번 행의 모든 램프가 켜져있다
    # 각 열별로 스위치 존재 -> j번 열의 스위치를 누를 켱우, 해당 열의 모든 램프 상태 변화
    # K번 스위치를 눌러서 켜져있는 행의 개수 최대로
    # 저번처럼 binary 이용하기에는 visited 크기가 2 ** (N*M)이라 메모리초과가 났음

    # zero_cnt[i] : i번 행에 포함된 0의 개수
    zero_cnt = [0] * N

    for i in range(N):
        # 각 행별로 0의 개수 세기
        c = 0
        for j in range(M):
            if arr[i][j] == 0:
                c += 1
        zero_cnt[i] = c

    # 켜진 최대 행의 개수
    result = 0

    # visited[i] : arr[i]와 같은 모양을 가진 행들에 대해 처리했는지 여부
    visited = [0] * N
    for i in range(N):
        # 각 행별로 0의 개수 파악
        # K번 안에 다 켤 수 있을 경우
        if zero_cnt[i] <= K:
            # 스위치 켜는 횟수와 시작의 0의 개수가 둘다 짝수 / 홀수여야 함
            # 아직 비교하지 않은 행 비교
            if abs(zero_cnt[i]-K)%2 == 0 and visited[i] == 0:
                visited[i] = 1
                # 본인과 같은 모양 세기
                cnt = 1
                # 다른 행들과 모양 비교 -> 같은 모양이면 한 번의 행동으로 똑같이 작용
                for y in range(N):
                    if y != i and arr[y] == arr[i]:
                        cnt += 1
                        visited[y] = 1
                if result < cnt:
                    result = cnt
    print(result)