# IM 대비 29. 퍼펙트 셔플
import sys
sys.stdin = open("퍼펙트셔플input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 카드 개수
    arr = list(input().split())

    result = [0] * N
    for i in range(N):
        if i%2:
            result[i] = arr[(i + N) // 2]
        else:
            result[i] = arr[i // 2]

    print(f'#{test_case}', end = ' ')
    for card in result:
        print(card, end = ' ')
    print()