# sw academy 노드의 합
import sys
sys.stdin = open("노드의합input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 노드 개수(1 <= N <= 1000)
    # M : 리프 노드 개수(1 <= N <= 1)
    # L : 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (1001) # 1 ~ N

    # 트리의 리프 노드 인덱스에 주어진 값 삽입
    for _ in range(M):
        leaf_idx, leaf_node = map(int, input().split())
        tree[leaf_idx] = leaf_node

    # 각 부모노드 : 자식노드 값들의 합합
    for i in range(N, 0, -1):
        if tree[i] == 0: # 아직 자식노드들로부터 못받은 경우
            tree[i] = tree[i*2] + tree[i*2+1]
    print(f'#{test_case} {tree[L]}')