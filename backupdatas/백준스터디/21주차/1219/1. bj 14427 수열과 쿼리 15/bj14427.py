import sys
sys.stdin = open("bj14427input.txt")

def build(node, start, end):
    if start == end:
        segment_tree[node] = arr[start]
        return segment_tree[node]
    mid = (start+end)//2
    segment_tree[node] = min(build(2 * node, start, mid), build(2 * node + 1, mid+1, end))
    return segment_tree[node]

def update(node, start, end, i, v):
    if i < start or i > end:
        return
    if start == end:
        segment_tree[node] = v
        return segment_tree[node]

    mid = (start+end)//2
    update(2 * node, start, mid, i, v)
    update(2 * node + 1, mid+1, end, i, v)
    segment_tree[node] = min(segment_tree[2 * node], segment_tree[2 * node + 1])

def find_min(node, start, end, left, right):
    if left > end or right < start:
        return [int(1e9), int(1e9)]

    if left <= start and right >= end:
        return segment_tree[node]

    mid = (start + end)//2
    return min(find_min(2 * node, start, mid, left, right), find_min(2 * node + 1, mid+1, end, left, right))
# N : 수열 내의 숫자 개수(1 <= N <= 100000)
N = int(input())
lst = list(map(int, input().split()))
arr = []
for i in range(1, N+1):
    arr.append([lst[i-1], i])
# print(arr)
segment_tree = [[] for _ in range(4 * N)]
build(1, 0, N-1)
# print(segment_tree)

# M : 쿼리문 개수(1 <= M <= 100000)
M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    # 1, i, v : i번째 index를 v로 바꾸기
    if query[0] == 1:
        i, v = query[1] - 1, query[2]
        arr[i][0] = v
        update(1, 0, N-1, i, arr[i])

    # 2 : 최소 값 찾기
    elif query[0] == 2:
        min_val = find_min(1, 0, N-1, 0, N-1)
        print(min_val[1])