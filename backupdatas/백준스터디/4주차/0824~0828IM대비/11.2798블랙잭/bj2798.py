# IM 대비 11. 백준 2798 블랙잭
import sys
sys.stdin = open("2798블랙잭input.txt")

T = int(input()) # 문제 제출시 없애기
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    subsets = []
    # M보다 작은 세 개의 카드로 이루어진 부분집합 생성
    # 이 경우는 부분집합이 3개라 그냥 모든 부분집합을 다 만들기보다는
    # 3개짜리 부분집합을 아예 만드는게 나은듯...시간초과 뜸
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if arr[i] + arr[j] + arr[k] <= M:
                    result = max(result, arr[i] + arr[j] + arr[k])
    '''
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(arr[j])
        if len(subset) == 3:
            result = sum(subset)
            if result == M:
                break
    '''
    print(result)






