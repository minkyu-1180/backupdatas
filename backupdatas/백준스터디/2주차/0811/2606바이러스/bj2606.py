# 백준 2606. 바이러스
import sys
sys.stdin = open("2606input.txt")
N = int(input()) # 컴퓨터의 수(<= 100)
K = int(input()) # 컴퓨터 쌍의 수
# i번 idx의 값 : i번 컴퓨터와 연결되어있는 컴퓨터 번호 리스트
arr = [[] for _ in range(N+1)]

for _ in range(K):
    start, end = map(int, input().split())
    # 양방향(컴퓨터 연결 네트워크)
    arr[start].append(end)
    arr[end].append(start)
# print(arr)

def DFS(arr, N, start):
    stack = []
    visited = [0] * (N+1)

    visited[start] = 1
    while True:
        # start 노드의 인접 노드들에 대해 for문 진행
        for next in arr[start]:
            if  visited[next] == 0: # 아직 방문 안한 노드가 있을 경우
                stack.append(start) # start를 스택에 추가 후 갱신
                start = next
                visited[start] = 1 # start의 인접 노드였던 것을 방문 후 for문에서 빠져나옴
                break
        # start노드의 인접 노드 중 만족하는 것이 없을 경우우
        else:
            # 스택이 비어있지 않은 경우
            if stack:
                start = stack.pop()
            else:
                break
    return visited

result = DFS(arr, N, 1)

# 1번 컴퓨터를 제외한 웜 바이러스에 걸린 컴퓨터의 수
print(result.count(1) - 1)