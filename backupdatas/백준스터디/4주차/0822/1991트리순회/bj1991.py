# 백준 1991. 트리 순회
import sys
sys.stdin = open("1991input.txt")

N = int(input()) # 이진 트리 노드 개수 (1 <= N <= 26)

tree = dict()

for i in range(N):
    p, lc, rc = list(input().split())
    tree.setdefault(p, []).append(lc)
    tree.setdefault(p, []).append(rc)

'''
def preorder(root):
    if root != '.':
        print(root, end = '')
        lc = tree[root][0]
        rc = tree[root][1]
        preorder(lc)
        preorder(rc)


def inorder(root):
    if root != '.':
        lc = tree[root][0]
        rc = tree[root][1]
        preorder(lc)
        print(root, end='')
        preorder(rc)


def postorder(root):
    if root != '.':
        lc = tree[root][0]
        rc = tree[root][1]
        preorder(lc)
        preorder(rc)
        print(root, end='')

'''
# 전위 순회
def preorder(root):
    if root != ".": # 자식이 있다면
        print(root, end="") # 루트 노드 출력
        preorder(tree[root][0]) # 재귀적으로 왼쪽 노드 탐색
        preorder(tree[root][1]) # 재귀적으로 오른쪽 노드 탐색


# 중위 순회
def inorder(root):
    if root != ".": # 자식이 있다면
        inorder(tree[root][0]) # 재귀적으로 왼쪽 노드 탐색
        print(root, end="") # 루트 노드 출력
        inorder(tree[root][1]) # 재귀적으로 오른쪽 노드 탐색


# 후위 순회
def postorder(root):
    if root != ".": # 자식이 있다면
        postorder(tree[root][0]) # 재귀적으로 왼쪽 노드 탐색
        postorder(tree[root][1]) # 재귀적으로 오른쪽 노드 탐색
        print(root, end="") # 루트 노드 출력



preorder('A')
print()
inorder('A')
print()
postorder('A')
print()