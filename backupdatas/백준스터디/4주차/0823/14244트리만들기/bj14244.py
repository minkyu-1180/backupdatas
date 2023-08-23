# 백준 14244. 트리 만들기
import sys
sys.stdin = open("14244input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 노드 개수
    # M : 리프노드 개수
    N, M = map(int, input().split())
    tree = [[] for _ in range(N)]
    if M == 2: # 엣지 개수가 2개 -> 한줄로 이어짐
        for i in range(N-1):
            tree[i].append(i+1)
    else:
        for i in range(1, M+1):
            tree[0].append(i)
        for i in range(M, N-1):
            tree[i].append(i+1)

    for i in range(N):
        if tree[i]:
            for adj in tree[i]:
                print(f'{i} {adj}')
