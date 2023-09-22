# swea 1486. 장훈이의 높은 선반

import sys
sys.stdin = open("swea1486input.txt")

def backtracking(c, sum_height):
    # 가지치기
    global result

    # 선반 높이를 막 넘었을 때 비교
    if B <= sum_height:
        result = min(result, sum_height)
        return

    if c == N:
        # result = min(result, sum_height)
        return

    backtracking(c+1, sum_height+arr[c])
    backtracking(c+1, sum_height)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = int(1e9)
    backtracking(0, 0)
    print(f'#{tc} {result-B}')

