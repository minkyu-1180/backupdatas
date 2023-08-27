# IM 대비 19. 최대 성적표 만들기
import sys
sys.stdin = open("최대성적표input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    result = 0 # K개의 성적합 최대값
    for _ in range(K):
        result += arr.pop()
    print(f'#{test_case} {result}')

    '''
    for i in range(1 << N):
        subsets = []
        for j in range(N):
            if i & (1 << j):
                subsets.append(arr[j])
        if len(subsets) == K and result < sum(subsets):
            result = sum(subsets)
    print(f'#{test_case} {result}')
    '''
