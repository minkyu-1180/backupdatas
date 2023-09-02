# 백준 18111. 마인크래프트
import sys
sys.stdin = open("bj18111input.txt")

T = int(input())
for tc in range(T):
    N, M, inventory = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_time = sys.maxsize # 최대 정수값(9223372036854775808)
    max_k = 0

    for k in range(267):
        over_v = 0
        under_v = 0

        for i in range(N):
            for j in range(M):
                if arr[i][j] >= k:
                    over_v += arr[i][j] - k
                else:
                    under_v += k - arr[i][j]
        # 모든 층을 k로 만들 수 있는 경우
        if over_v + inventory >= under_v and under_v + over_v * 2 <= min_time:
            # 현재 최저시간과 비교 후 갱신
            min_time = under_v + over_v * 2
            max_k = k

    print(min_time, max_k)
