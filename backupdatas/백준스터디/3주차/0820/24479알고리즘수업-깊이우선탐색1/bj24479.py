# 백준 24479. 알고리즘수업 - 깊이우선탐색 1
import sys
sys.stdin = open("24479input.txt")

def DFS(start):
    global c
    visited[start] = c # 방문 노드에 순서 삽입
    for next in adj[start]:
        if visited[next] == 0:
            c += 1
            DFS(next)



# N : 정점의 수 (5 ~ 100000)
# M : 간선의 수 (1 ~ 200000)
# R : 시작 정점 (1 ~ N)
N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
c = 1 # 방문 순서

# 인접노드 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

# 인접노드에 오름차순으로 접근할 수 있도록 정렬
for nodes in adj:
    nodes.sort()


DFS(R)
for i in range(1, N+1):
    print(visited[i])