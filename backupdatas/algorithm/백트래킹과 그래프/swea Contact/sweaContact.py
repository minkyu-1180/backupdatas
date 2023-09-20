# swea. Contact
import sys
from collections import deque
sys.stdin = open("Contactinput.txt")

def bfs():
    result = 0
    while que:
        now = que.popleft()

        if graph[now]:
            for next in list(graph[now]):
                if visited[next] == -1:
                    visited[next] = visited[now] + 1
                    if visited[next] > result:
                        result = visited[next]
                    que.append(next)
    return result


for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [set() for _ in range(101)]
    for i in range(0, N, 2):
        graph[arr[i]].add(arr[i+1])

    visited = [-1] * 101
    visited[start] = 0
    que = deque()
    que.append(start)
    max_val = bfs()
    result = 0

    # print(visited)
    for i in range(100, 0, -1):
        if visited[i] == max_val:
            result = i
            break
    print(f'#{tc} {result}')
