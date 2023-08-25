# IM 대비 12. 특별한 정렬
import sys
sys.stdin = open("특별한정렬input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 정수 개수(10 <= N <= 100)
    arr = list(map(int, input().split())) # N개의 정수(1 ~ 100)
    arr.sort() # 오름차순으로 정리
    result = [0] * N # 특별한 정렬 결과 담기

    for i in range(N//2):
        result[i*2 + 1] = arr[i]
    for i in range(N-1, N//2-1, -1):
        result[((N-1)-i)*2] = arr[i]

    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(result[i], end = ' ')
    print()