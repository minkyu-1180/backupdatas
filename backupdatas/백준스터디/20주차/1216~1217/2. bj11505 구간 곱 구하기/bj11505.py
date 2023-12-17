import sys
sys.stdin = open("bj11505input.txt")

# 세그먼트 트리 생성
def build(node, left, right):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree[node]
    mid = (left + right)//2
    segment_tree[node] = (build(2 * node, left, mid) * build(2 * node + 1, mid+1, right))%1000000007
    return segment_tree[node]

# 구간합
# start, end : b, c
def find_sum(start, end, node, left, right):
    # 구간을 벗어난 경우
    if end < left or start > right:
        return 0
    # 완벽하게 포함된 경우
    if start <= left and end >= right:
        return segment_tree[node]

    mid = (left + right)//2
    return find_sum(start, end, 2 * node, left, mid) + find_sum(start, end, 2 * node + 1, mid+1, right)
def find_multi(start, end, node, left, right):
    # 구간을 벗어난 경우
    if end < left or start > right:
        return 1
    # 완벽하게 포함된 경우
    if start <= left and end >= right:
        return segment_tree[node]

    mid = (left + right)//2
    return (find_multi(start, end, 2 * node, left, mid) * find_multi(start, end, 2 * node + 1, mid+1, right)) % 1000000007



# 업데이트
# index : b-1
# c : b-1번 노드를 바꿀 목표값
def update(node, left, right, index, c):
    # 끝
    if left == right == index:
        segment_tree[node] = c
        return

    # 범위에 포함 X
    if index < left or index > right:
        return
    mid = (left+right)//2
    update(2 * node, left, mid, index, c)
    update(2 * node + 1, mid+1, right, index, c)
    # 자식 노드를 통해 부모 노드 업데이트
    segment_tree[node] = (segment_tree[2 * node] * segment_tree[2 * node + 1]) % 1000000007
# N : 수의 개수(1 <= N <= 1000000)
# M : 수의 변경이 일어나는 횟수(1 <= M <= 10000)
# K : 구간의 곱을 구하는 횟수(1 <= K <= 10000)
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input().rstrip()))
# 세그먼트 트리 생성
segment_tree = [0] * (4 * N)
build(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    # a = 1 -> b번째 수를 c로 바꾸기
    if a == 1:
        update(1, 0, N-1, b-1, c)
    # a가 2인 경우 : b번째 수부터 c번째 수까지의 곱을 1000000007로 나눈 나머지 출력
    elif a == 2:
        print(find_multi(b-1, c-1, 1, 0, N-1))