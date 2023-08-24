# IM 대비 4. minmax
import sys
sys.stdin = open("minmaxinput.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 주어진 양수 개수(5 <= N <= 1000)
    arr = list(map(int, input().split())) # N개의 양의 정수

    # result[0] : min
    # result[1] : max
    result = [arr[0], arr[0]]
    for i in range(1, N):
        # 최솟값 갱신
        if result[0] > arr[i]:
            result[0] = arr[i]
        # 최댓값 갱신
        if result[1] < arr[i]:
            result[1] = arr[i]
    # 결과 : 최대 - 최소
    ans = result[1] - result[0]
    print(f'#{test_case} {ans}')