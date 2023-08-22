# sw academy 이진힙
import sys
sys.stdin = open("이진힙input.txt")

# 최소 힙 반환
def min_heap(arr, N):
    tree = [0] * (N + 1)
    tree[1] = arr[0]
    for i in range(2, N+1):
        tree[i] = arr[i-1]
        idx = i
        while idx > 1:
            # 부모 노드값이 자식노드값보다 큰 경우(최소힙 위배)
            if tree[idx//2] > tree[idx]:
                tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
                idx //= 2
            else:
                break
    return tree

# 해당 노드의 조상노드값들의 합
def ancestor_sum(tree, N): # 최소 힙 / 조상노드들의 합을 알고싶은 노드
    idx = N
    result = 0
    while idx > 1: # 루트 노드 idx : 1
        idx //= 2 # 해당 노드의 부모노드에 접근
        result += tree[idx]
    return result # idx == 1이 되는 순간, 결과값(N번 노드의 조상 노드들의 값의 합) 반환


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 5 <= N <= 500
    arr = list(map(int, input().split())) # 각 원소 : 1 ~ 1000000
    # 최소힙 만들기(부모 노드값 < 자식 노드값)
    # 마지막 노드의 조상 노드에 저장된 정수의 합
    tree = min_heap(arr, N)
    result = ancestor_sum(tree, N)
    print(f'#{test_case} {result}')
