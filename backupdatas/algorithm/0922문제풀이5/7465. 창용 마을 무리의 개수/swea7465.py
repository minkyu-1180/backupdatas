# swea 7465. 창용마을 무리의 개수
import sys
sys.stdin = open("swea7465input.txt")

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        union(s, e)
    # graph = [[] for _ in range(N+1)]
    # for _ in range(M):
    #     s, e = map(int, input().split())
    #     graph[s].append(e)

    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))

    print(f'#{tc} {len(result)}')

