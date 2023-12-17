# 백준 2357. 최솟값과 최댓값
# 세그먼트 트리 클래스 작성
import sys
sys.stdin = open("bj2357input.txt")
'''
세그먼트 트리 : 특정 구간에 대한 질문을 빠르게 대답하게 위해 쓰이는 꽉찬 이진 트리 형태의 자료구조
min, max 함수 : O(N) -> 시간초과일때 사용
- 루트 : 전체 구간의 정보를 담고 있다
- 왼쪽 자식 노드와 오른쪽 자식 노드 : 부모 노드가 표현하는 구간의 왼쪽 절반에 대한 정보, 오른쪽 절반에 대한 정보 포함
- 구간을 절반씩 나누어서 정보 포함 -> O(logN)안에 구간의 최솟값, 최댓값을 구할 수 있다
'''

class SegmentTree:
    def __init__(self, N, arr):
        self.N = N # 주어진 원소 개수(노드 번호 주기)
        self.arr = arr
        # 왜 범위가 4 * N으로 된거징?
        self.min_tree = [0] * (4 * N)
        self.max_tree = [0] * (4 * N)
        self.INT_MAX = int(1e15) # 최대 숫자 : 1,000,000,000
        self.INT_MIN = 0

        # 트리 초기화
        self.min_init(0, N-1, 1)
        self.max_init(0, N-1, 1)

    # 세그먼트 트리의 idx번 노드의 최솟값?
    def min_init(self, left, right, idx):
        # 범위 내의 값이 한 개일 경우 구할 필요 없이 바로 리턴
        if left == right:
            self.min_tree[idx] = self.arr[left]
            return self.min_tree[idx]

        # 아닐 경우 재귀
        mid = (left+right)//2
        # 왼쪽 재귀 vs 오른쪽 재귀 비교해서 min값 넣어주기
        self.min_tree[idx] = min(self.min_init(left, mid, 2*idx),
                                 self.min_init(mid+1, right, 2*idx+1))
        return self.min_tree[idx]

    # 세그먼트 트리의 idx번 노드의 최댓값?
    def max_init(self, left, right, idx):
        # 범위 내의 값이 한 개일 경우 구할 필요 없이 바로 리턴
        if left == right:
            self.max_tree[idx] = self.arr[left]
            return self.max_tree[idx]
        mid = (left+right)//2
        # 왼쪽 재귀 vs 오른쪽 재귀 비교해서 min값 넣어주기
        self.max_tree[idx] = max(self.max_init(left, mid, 2*idx),
                                 self.max_init(mid+1, right, 2*idx+1))
        return self.max_tree[idx]

    '''
    left, right : 범위(a, b)
    idx : 현재 노드 번호
    left_node, right_node : 시작, 끝 노드 번호
    '''
    def min_query(self, left, right, idx, left_node, right_node):
        # 노드 범위 올바르지 못할 경우 -> 최대값 출력
        if left_node > right or right_node < left:
            return self.INT_MAX

        # 범위가 올바르게 들어오는 경우
        if left <= left_node and right_node <= right:
            return self.min_tree[idx]

        mid = (left_node + right_node) // 2
        return min(self.min_query(left, right, 2 * idx, left_node, mid),
                   self.min_query(left, right, 2 * idx + 1, mid + 1, right_node))

    def max_query(self, left, right, idx, left_node, right_node):
        # 노드 범위 올바르지 못할 경우 -> 최솟값 출력
        if left_node > right or right_node < left:
            return self.INT_MIN

        # 범위가 올바르게 들어오는 경우
        if left <= left_node and right_node <= right:
            return self.max_tree[idx]

        mid = (left_node + right_node) // 2
        return max(self.max_query(left, right, 2 * idx, left_node, mid),
                   self.max_query(left, right, 2 * idx + 1, mid + 1, right_node))

    # 범위가 주어질 때, 해당 범위 내의 최소/최대값 반환
    def find(self, left, right):
        return self.min_query(left, right, 1, 0, self.N - 1), self.max_query(left, right, 1, 0, self.N - 1)

# N : 정수의 개수(1 <= N <= 100000)
# M : a, b의 쌍 개수(1 <= M <= 100000)
N, M = map(int, input().split())
arr = []
for _ in range(N):
    # 주어지는 정수값 : 1 ~ 1000000000
    arr.append(int(input()))

# 주어진 배열을 세그먼트 트리로 만들기
segment_tree = SegmentTree(N, arr)

tree_min = segment_tree.min_tree
tree_max = segment_tree.max_tree
'''
                0   
       5                  30
    5    30            38    20
 5    30 100 38     50    51  20  81

'''
# print(tree_min)
for _ in range(M):
    # a, b쌍 : a번째 정수부터 b번째 정수까지 중에서 최솟값, 최댓값 출력
    a, b = map(int, input().split())
    min_v, max_v = segment_tree.find(a-1, b-1)
    print(min_v, max_v)