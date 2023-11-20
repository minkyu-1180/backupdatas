# 백준 15591. MooTube(Silver)
import sys
sys.stdin = open("bj15591input.txt")
sys.setrecursionlimit(10**5)

def dfs(start, now):
    visited[now] = 1
    for next, dist in graph[now]:
        if next != start and visited[next] == 0:
            if USADO[now] > dist:
                USADO[next] = dist
            else:
                USADO[next] = USADO[now]
            dfs(start, next)


# N : 이미 올려진 동영상 개수 (1 <= N <= 5000)
# Q : 질문의 개수
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
# graph = [[int(1e9)] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    # p와 q 동영상이 USADO r로 연결되어있다
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

# USADO = [[0] * (N+1) for _ in range(N+1)]
# for node in range(1, N+1):
#     dfs(node)
for _ in range(Q):
    # K : USADO가 K 이상인 모든 동영상이 추천되도록
    # 만약 K = k일 때, 동영상 v를 보고 있는 소들에게 몇 개의 동영상이 추천될까요?
    k, v = map(int, input().split())

    # USADO[i] : k -> i로 갈 때 USADO값
    USADO = [int(1e9)] * (N+1)
    visited = [0] * (N+1)
    dfs(v, v)
    # print(USADO)

    result = 0
    for i in range(1, N+1):
        if i == v or USADO[i] < k:
            continue
        result += 1

    print(result)
# print(graph)