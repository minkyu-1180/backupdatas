# sw academy contact
import sys
sys.stdin = open("contactinput.txt")

def bfs(start, adj):
    queue = []
    visited = [0] * (101)
    last_num = 0
    last_idx = 0 # 가장 늦게 연락받은 번호 중, 가장 큰 번호

    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.pop(0)
        # print(node, visited[node])
        # 방향 그래프
        # 해당 노드가 시작으로 하는 간선이 있을 경우
        # 받는 역할의 노드가 queue에 추가된 것을 방지

        for next in adj[node]:
            if visited[next] == 0:
                # 방향 고려(시작 -> 끝에서 끝이 시작이 될 수 있는 경우)
                if next in adj.keys():
                    queue.append(next)
                    visited[next] = visited[node] + 1
                # 끝이 시작이 될 수 없는 경우
                else:
                    visited[next] = visited[node] + 1

    # 가장 늦게 방문한 번호 중, 가장 큰 번호 갱신
    for i in range(1, 101):
        if visited[i] != 0 and last_num <= visited[i]:
            last_num = visited[i]
            last_idx = i

    return last_idx


for test_case in range(1, 11):
    N, start = map(int, input().split()) # N : 총 개수 / start : 시작점
    arr = list(map(int, input().split())) # [from, to, from, to, ,,,]

    adj = dict()
    # 인접 리스트 생성
    for i in range(0, len(arr), 2):
        # 중복 제거
        adj.setdefault(arr[i], list(set())).append(arr[i+1])
    print(f'#{test_case} {bfs(start, adj)}')
