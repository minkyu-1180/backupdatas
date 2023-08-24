# IM 대비 9. 두 개의 숫자열
import sys
sys.stdin = open("두개의숫자열input.txt")


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 더 긴 배열은 고정
    # 더 짧은 배열을 움직이며 진행
    '''
    max_len : 더 큰 배열의 길이
    min_len : 더 작은 배열의 길이
    max_arr : 더 긴 배열
    min_arr : 더 짧은 배열
    '''
    if N >= M:
        max_len = N
        max_arr = A
        min_arr = B
        min_len = M
    else:
        max_len = M
        max_arr = B
        min_arr = A
        min_len = N

    result = 0 # 결과를 담을 변수
    for i in range(max_len - min_len + 1):
        # 시작점이 i일 때 구간합을 담을 변수
        i_sum = 0
        for j in range(min_len):
            i_sum += (max_arr[i+j] * min_arr[j]) # 마주보고 있는 값의 곱을 더하기
        if result < i_sum:
            result = i_sum
    print(f'#{test_case} {result}')