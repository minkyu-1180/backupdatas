# sw academy 이진탐색
import sys
sys.stdin = open("이진탐색input.txt")

# 트리 생성 함수(조건 O)
# 조건 : 왼쪽 자식 노드 < 서브트리의 루트 노드 < 오른쪽 자식 노드
'''
def make_tree(tree, idx, start, end, N):
    if idx > N:
        return
    
    node = (start + end) // 2 + (start+end) % 2
    tree[idx] = node

    make_tree(tree, idx * 2, start, node-1, N)
    make_tree(tree, idx * 2+1, node+1, end, N)
'''

def make_tree(idx):
    global node
    if idx <= N:
        make_tree(idx*2)
        tree[idx] = node
        node += 1
        make_tree(idx*2+1)



T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 1 <= N <= 1000
    # 이진 탐색 트리 규칙 : 왼쪽 서브트리 루트 < 현재 노드 < 오른쪽 서브트리 루트
    tree = [0] * (N+1)
    node = 1
    make_tree(1)
    print(tree)
    print(f'#{test_case} {tree[1]} {tree[N//2]}')
