# 백준 16562. 친구비
import sys
sys.stdin = open("bj16562input.txt")

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x = find(x)
    y = find(y)

    # if x != y:
    if arr[x] >= arr[y]:
        parent[x] = y
    else:
        parent[y] = x


# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 학생 수(1 <= N <= 10000)
    # M : 친구관계 수(0 <= M <= 10000)
    # k : 가지고 있는 돈(1 <= k <= 10000000)
    N, M, k = map(int, input().split())
    # arr : 각 학생이 원하는 친구비 목록
    arr = [0] + list(map(int, input().split()))
    parent = [x for x in range(N+1)]
    for _ in range(M):
        # v와 w는 친구이다
        # 자기 자신과 친구일수도
        # 같은 친구 관계가 여러번 주어질 수도
        v, w = map(int, input().split())
        union(v, w)

    result = 0
    for i in range(1, N+1):
        # 최상단 부모가 자기 자신인 놈들 찾기 -> 그러면 친구비 감소 가능
        if parent[i] == i:
            result += arr[i]
    # print(result)
    if result <= k:
        print(result)
    else:
        print("Oh no")