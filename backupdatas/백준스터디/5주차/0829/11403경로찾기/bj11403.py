# 백준 11403. 경로찾기
import sys
sys.stdin = open("11403input.txt")

def dfs(N, adj, i, j):
    visited = [[0] * N for _ in range(N)] # [i][j] : i -> j로 간 적 있나요?
    stack = []
    length = 0 # i -> i 경로가 있는 경우 예외케이스 확인을 위한 변수

    start = i
    end = j
    while True:
        if start == end and length > 0: # 둘이 같아지고, 거리가 양수일 경우
            arr[i][j] = 1
            break

        for next in range(N):
            # 현재 방문중인 start의 인접 노드들 중 방문하지 않은 노드 찾기
            if adj[start][next] == 1 and visited[start][next] == 0:
                stack.append(start)
                visited[start][next] = 1 # next 방문 후 start로 갱신
                start = next
                length += 1 # 현재 길이값
                break
        else:
            if stack:
                start = stack.pop()
                length -= 1 # dfs 특징 : stack[-1]로 되돌아가기 -> length -= 1
            else:
                break



T = int(input())
for test_case in range(T):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(N, adj, i, j)

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()
