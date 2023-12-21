# 백준 1777. 순열 복원
import sys
sys.stdin = open("bj1777input.txt")

def build(node, left, right):
    # left == right -> 해당 node 빌드
    if left == right:
        segment_tree[node] = 1
        return segment_tree[node]

    mid = (left + right)//2
    # 자식 노드 재귀
    segment_tree[node] = build(2 * node, left, mid) + build(2 * node + 1, mid+1, right)
    return segment_tree[node]

def update(node, left, right, index):
    if index < left or index > right:
        return

    # 역순으로 update 진행
    segment_tree[node] -= 1
    if left == right:
        return

    mid = (left + right)//2
    update(2 * node, left, mid, index)
    update(2 * node + 1, mid+1, right, index)
# 우리가 필요한 값 : 복원된 순열의 특정 인덱스에 들어갈 값
def query(node, left, right, value):
    if left == right:
        return left
    # 아닐 경우
    mid = (left + right)//2
    # inversion sequence의 값과 segment tree의 자식 노드와 비교
    # 현재 비어있는 칸의 개수가 더 많을 경우 -> 오른쪽 자식 노드에서 찾기
    if value < segment_tree[2 * node + 1]:
        return query(2 * node + 1, mid+1, right, value)
    # 더 적을 경우 -> 왼쪽 자식노드에서 찾기
    # 오른쪽 자식 노드의 값만큼 빼고 찾기(기존에는 양쪽을 더해주는 형태)
    found = segment_tree[2*node+1]
    return query(2 * node, left, mid, value - found)
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 순열의 크기(1 <= N <= 100000)
    N = int(input())
    # Inversion Sequence
    arr = list(map(int, input().split()))
    # 결과(복원된 순열)
    result = [0] * N
    # segment_tree[node] : left ~ right 사이에 비어있는 arr index 번호 개수
    segment_tree = [0] * (4 * N)

    # 세그먼트 트리 초기화
    build(1, 0, N-1)
    for i in range(N, 0, -1):
        # arr[i] : 순열에서 i보다 뒤에 나오면서 i보다 작은 수의 개수
        # 뒤에서부터 찾아야 앞에서는 이미 찾은 아이들이 들어간 상태로 시작
        value = arr[i-1]
        index = query(1, 0, N-1, value)
        # 복원된 순열의 index 번 값은 현재 i값
        result[index] = i
        # 찾은 index update
        update(1, 0, N-1, index)
    print(result)