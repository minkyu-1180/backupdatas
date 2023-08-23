# 백준 20364. 부동산 다툼
import sys
sys.stdin = open("20364input.txt")
T = int(input())
for test_case in range(1, T+1):
    # N : 땅 개수 (2 <= N < 2^20) / Q : 꽉꽉나라 오리 수 (1 <= Q <= 200000)
    N, Q = map(int, input().split())
    '''
    루트 노드 : 1
    왼-자 : 2*K / 오-자 : 2*k+1
    '''
    result = [] # 결과를 담을 리스트
    # 조상노드 만들기
    # 리스트의 idx : 현재 노드
    # 해당 idx의 값(리스트)의 원소 : 조상노드(descending)
    # 추가적으로 자기 자신도 해당 값에 넣었음
    # 본인이 사려는 땅의 기존 구입여부도 확인 필요
    parent = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        p = i
        while p:
            parent[i].append(p)
            p //= 2
        parent[i].sort() # 최고조상부터 보기 위해 정렬

    arr = [0] * (Q+1) # i번 오리가 원하는 땅 번호를 담을 리스트
    for i in range(1, Q+1):
        arr[i] = int(input()) # 각 값 : 2 ~ N(루트 노드는 안먹는 구조)

    state = [0] * (N+1) # 현재 각 땅의 구입상태
    for i in range(1, Q+1):
        land = arr[i] # 현재 사려고 하는 땅의 번호
        for p in parent[land]: # 현재 사려고 하는 땅의 조상 노드들(본인 포함)에 대해 반복
            if state[p]: # 조상 노드가 구매되었을 경우
                result.append(p) # 처음 만난 구매된 조상노드 번호를 결과로 담기
                break

        # for문에서 break가 걸리지 않은 경우 구입 가능
        else:
            result.append(0) # 해당 땅 구입
            state[land] = 1  # 해당 땅 구입 표시

    for r in result:
        print(r)
