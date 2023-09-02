# 백준 1783. 병든 나이트
import sys
sys.stdin = open("bj1783input.txt")

T = int(input())
for tc in range(T):
    # N, M : 체스판의 세로 / 가로 길이(1 <= N, M <= 2,000,000,000)
    N, M = map(int, input().split())
    # 가장 왼쪽 아래 칸에 병든 나이트 위치
    '''
    병든 나이트가 움직일 수 있는 방법
    1. 2칸 위로, 1칸 오른쪾
    2. 1칸 위로, 2칸 오른쪽
    3. 1칸 아래로, 2칸 오른쪽
    4. 2칸 아래로, 1칸 오른쪽
    '''
    if N == 1:
        result = 1
    elif N == 2:
        if 1 <= M <= 6:
            result = (M+1)//2
        else:
            result = 4
    elif N >= 3:
        if 1 <= M <= 4:
            result = M
        elif M == 5 or M == 6:
            result = 4
        else:
            result = M - 2

    print(result)