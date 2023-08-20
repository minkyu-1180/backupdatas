import sys
sys.stdin = open("1260input.txt")
from collections import deque

# n: 정점의 개수, m: 간선의 개수, v:탐색을 시작할 정점의 번호
N, M, start = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N + 1)]

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
    adj[v1].sort()
    adj[v2].sort()


def DFS(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for next in adj[start]:
        if visited[next] == 0:
            DFS(graph, next, visited)


# BFS 함수 정의
def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for next in graph[node]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = 1


visited = [0] * (N + 1)
DFS(adj, start, visited)
print()
visited = [0] * (N + 1)
BFS(adj, start, visited)