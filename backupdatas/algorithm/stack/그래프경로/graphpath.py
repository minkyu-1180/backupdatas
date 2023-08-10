# 그래프 경로
import sys
sys.stdin = open('graphpathinput.txt')

def DFS(start, V, adj_matrix): # 인접 매트릭스, 시작노드 제공
    # 방문 노드 배열 / 스택 초기화
    visited = [0] * (V+1) # i번 idx에 i번 노드의 방문여부 할당
    stack = []

    # 시작노드 방문
    visited[start] = 1
    # print(start)
    # 종료 조건 : start가 정해진 상태에서 start와 인접하거나 방문하지 않은 노드가 하나도 없을 때
    # 동시에, stack이 빈 상태일 때(DFS 시행 완료일 때)
    while True:
        # next : start와 인접한지 확인하려는 노드
        for next in range(1, V+1):
            # 인접하면서 동시에 아직 방문하지 않았을 때
            # stack에 현재 방문중인 노드를 push해주고, 인접 노드를 start로 갱신 후 방문
            # if문에 해당되는 경우, 뒤의 인접노드들은 볼 필요 X -> for문에서 빠져나오기
            if adj_matrix[start][next] == 1 and visited[next] == 0:
                stack.append(start)
                start = next
                # print(start)
                visited[start] = 1
                break
        # 모든 노드들에 대해 현재 방문 노드와의 관계를 확인했지만, 조건에 부합하지 않는 경우
        else:
            # 스택이 비어있지 않은 경우(즉, 다시 왔던 길을 되돌아감으로써 빠진 길이 없나 찾아볼 경우)
            if stack:
                # start 갱신
                start = stack.pop()
            # 스택이 빈 경우 : 끝!
            else:
                break
    # 노드들의 최종 방문 여부 확인
    return visited


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())

    # vertex간의 인접 여부를 확인하는 배열
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        # 엣지를 형성하는 두 노드들에 대한 정보
        s, e = map(int, input().split())
        # i -> j인 edge가 존재할 경우 arr[i][j] = 1
        adj_matrix[s][e] = 1

    # S에서 G로 가는 Path가 존재하는가?
    S, G = map(int, input().split())

    # DFS 시행 후 방문 리스트를 변수에 할당
    # i번 idx의 값이 1 : 방문 경험 O
    # i번 idx의 값이 0 : 방문 경험 X 즉, DFS동안 방문한 적이 없음
    result = DFS(S, V, adj_matrix)

    # result의 G번 idx의 값이 0인 경우 : DFS를 시행했음에도 불구하고 방문 실패
    # result의 G번 idx의 값이 1인 경우 : S에서 G로 가는 길이 있다!
    print(f'#{test_case} {result[G]}')