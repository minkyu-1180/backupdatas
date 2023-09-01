# 부분수열의 합
import sys
sys.stdin = open("부분수열input.txt")

# 두 번째 방법
def subset(s, i, N, K, rs):
    global cnt
    if i == N:
        if s == K:
            cnt += 1
    elif s > K:
        return
    elif s+rs < N:
        return
    else:
        subset(s + arr[i], i+1, N, K, rs-arr[i])
        subset(s, i+1, N, K, rs-arr[i])


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    c = 0

    for i in range(1 << N): # 모든 부분집합
        s = 0 # 해당 부분집합의 합
        for j in range(N):
            if i & (1 << j): # j번 비트가 1일 경우(해당 원소는 현재 부분집합에 포함)
                s += arr[j]  # 부분집합에 포함된 숫자 추가
        if s == K:
            c += 1
    print(f'#{test_case} {c}')

    cnt = 0
    subset(0, 0, N, K)
    print(f'#{test_case} {cnt}')

