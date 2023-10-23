# 백준 1915. 가장 큰 정사각형
import sys
sys.stdin = open("bj1915input.txt")

# N : 주어진 2차원 배열의 세로 크기(1 <= N <= 1000)
# M : 주어진 2차원 배열의 가로 크기(1 <= M <= 1000)
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# arr = [list(map(int, input())) for _ in range(N)]
for lst in arr:
    print(lst)
# print(arr)
make_rectangular = [[0] * M for _ in range(N)]

max_length = 0
for i in range(N):
    for j in range(M):
        # 현재 위치의 배열 값
        value = int(arr[i][j])
        value = arr[i][j]
        # value = 1 -> 진행 가능
        if value:
            # 대각선 위, 왼쪽, 위 다 볼 수 있을 떄
            if 0 <= i-1 < N-1 and 0 <= j-1 < M-1:
                # 가장 작은 값의 의미
                # 자기 기준으로 앞쪽에 구간을 잡았을 때, 얼마나 큰 정사각형을 만들 수 있나요?
                # 따라서, 그 중 교집합을 찾기 위해 min값을 잡고, 그것을 기준으로 1칸씩 세로 가로 더해줌
                # -> + 1
                make_rectangular[i][j] = min(make_rectangular[i-1][j-1], make_rectangular[i-1][j], make_rectangular[i][j-1]) + 1
            # 아닌 경우 : 벽에 붙어있음 -> 어차피 1임
            else:
                make_rectangular[i][j] = 1
            # 정사각형 최대 길이 갱신
            if max_length < make_rectangular[i][j]:
                max_length = make_rectangular[i][j]
        # arr[i][j] = 0 -> make_rectangular[i][j] = 0 too
        else:
            make_rectangular[i][j] = 0
# for lst in make_rectangular:
#     print(lst)
print(max_length**2)