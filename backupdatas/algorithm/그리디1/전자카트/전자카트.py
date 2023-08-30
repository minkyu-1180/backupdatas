# sw academy 전자카트
def perm(i, N):
    if i == N:
        one = [0] + p + [0]
        cases.append(one)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            perm(i+1, N)
            p[i], p[j] = p[j], p[i]

'''
	
정인성[서울_3반]
오후 3:18
def comb(n):
    if len(n) == N:
        stack.append(n + [1])
        return
    for i in range(2, N+1):
        if not visited[i]:
            visited[i] = True
            comb(n + [i])
            visited[i] = False

'''

import sys
sys.stdin = open("전자카트input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 방 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = list(range(1, N))
    cases = []
    perm(0, N-1)
    min_v = 10000000
    for case in cases:
        c = 0
        for i in range(1, len(case)):
            c += arr[case[i-1]][case[i]]
        if min_v > c:
            min_v = c
    print(f'#{test_case} {min_v}')
