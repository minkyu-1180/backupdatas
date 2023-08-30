# 백준 17471. 게리맨더링
import sys
sys.stdin = open("게리맨더링input.txt")

def people(subset):
    c = 0
    for num in subset:
        c += arr[num]
    return c

def bfs(subset):
    if len(subset) == 1:
        return True
    visited = dict()
    c = 0
    for node in subset:
        visited[node] = 0

    start = subset[0]
    visited[start] = 1
    c += 1
    que = [start]

    while que:
        now = que.pop(0)
        for next in graph[now]:
            if next in visited.keys() and visited[next] == 0:
                visited[next] = 1
                c += 1
                if c == len(subset):
                    return True
                que.append(next)

    return False


T = int(input())
for test_case in range(1, T+1):

    N = int(input()) # 구역 수
    arr = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]

    area_num = list(range(1, N+1))
    for i in range(1, N+1):
        adj_info = list(map(int, input().split()))
        for j in range(1, len(adj_info)):
            if adj_info[0] != 0:
                graph[i].append(adj_info[j])

    result = 1001
    for i in range(1 << N):
        sub1 = []
        sub2 = []
        for j in range(N):
            if i & (1 << j):
                sub1.append(area_num[j])
            else:
                sub2.append(area_num[j])
        if sub1 and sub2 and len(sub1) <= len(sub2):
            if bfs(sub1) and bfs(sub2):
                diff = abs(people(sub2) - people(sub1))
                if result > diff:
                    result = diff
    if result == 1001:
        result = -1

    print(result)


