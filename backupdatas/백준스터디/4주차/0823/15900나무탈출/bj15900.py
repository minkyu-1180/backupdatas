# 백준 15900. 나무 탈출



#T = int(input())
#for test_case in range(1, T+1):
# 트리의 정점 개수(2 <= N <= 500000)
import sys
sys.stdin = open("15900input.txt")


N = int(input())

# 인접관계
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def dfs(root, N, adj):
    result = 0
    c = 0
    stack = []
    visited = [0] * (N+1)
    visited[root] = 1 # 루트 노드 방문처리

    while True:
        for next in adj[root]:
            if visited[next] == 0:
                stack.append(root)
                root = next
                visited[root] = 1
                c += 1
                break
        else:
            # 스택에 들어있을 경우
            if stack:
                if len(adj[root]) == 1:
                    # 루트 노드에서 리프 노드까지의 간선 개수 추가
                    result += c
                # 이미 한 칸 더 갔으니까 count 한 개 빼주기
                c -= 1
                root = stack.pop()
            else:
                break
    return result

result = dfs(1, N, adj)

if result % 2:
    print('Yes')
else:
    print('No')


