# IM 대비 1. 파리퇴치
import sys
sys.stdin = open("파리퇴치input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N(5 <= N <= 15) : 배열 크기
    # M(2 <= M <= N) : 파리채 크기
    N, M = map(int, input().split())
    # N x N의 매트릭스에 각 원소 값 : 앉아있는 파리 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0 # 내려칠 때 잡는 최대값 구하기
    # i, j 조건 : 0 <= i, j <= N-M
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ij = 0 # (i, j) ~ (i+M-1, j+M-1) 사이의 파리 총합을 담을 변수
            for y in range(M):
                for x in range(M):
                    sum_ij += arr[i+y][j+x]
            if result < sum_ij: # 현재 최대값보다 큰 경우 갱신
                result = sum_ij

    print(f'#{test_case} {result}')

