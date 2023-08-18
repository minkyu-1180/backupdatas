# sw academy 노드의 거리
import sys
sys.stdin = open("노드의거리input.txt")


# start와 end의 방문 차이를 반환할 함수
# 만약, start에서 bfs 실행 시 end로 가지 않은 경우, 음수값 반환
def bfs(start, end, N):
    visited = [0] * (V+1)
    queue = []

    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.pop(0)
        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[node] + 1
    if visited[end] == 0:
        return 0
    return visited[end] - visited[start]

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # 노드개수, 엣지개수 : 5 <= V <= 50 / 4 <= E <= 1000
    arr = [list(map(int, input().split())) for _ in range(E)] # 그래프 간선 관계 노드 표시
    start, end = map(int, input().split()) # 시작점, 끝점 표시
    '''
    print(V, E)
    print(arr)
    print(start, end)
    '''
    # 인접 노드들을 표현한 배열
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i]
        adj[v1].append(v2)
        adj[v2].append(v1)

    # 시작점에서 bfs를 시작했을 때, end와 start 사이의 거리
    # bfs 실행 시 end에 가지 않은 경우, 음수값
    result = bfs(start, end, V)

    print(f'#{test_case} {result}')

