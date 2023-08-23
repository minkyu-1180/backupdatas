# 백준 4803. 트리
import sys
sys.stdin = open("4803input.txt")

def dfs(start, N, adj):
    visited = [0] * (N+1)
    stack = []

    visited[start] = 1
    while True:
        for next in adj[start]:
            if visited[next] == 0:
                stack.append(start)
                start = next
                visited[start] = 1
        else:
            if stack:
                if visited[stack[-1]] = 1



N, M = map(int, input().split())
case = 1
while N != 0 and M != 0:
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)


    print(adj)


    case += 1
    N, M = map(int, input().split())
