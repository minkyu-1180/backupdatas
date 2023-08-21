# sw academy subtree
import sys
sys.stdin = open("subtreeinput.txt")
T = int(input())
for test_case in range(1, T+1):
    # E : 간선의 개수 / N : 서브트리의 루트
    # 노드 번호 : 1 ~ (E+1) (1 <= E <= 1000 / 1 <= N <= E+1)
    E, N = map(int, input().split())
    arr = list(map(int, input().split())) # E개의 부모-자식 노드쌍
    # 부모 - 자식 노드 번호 사이에 특별한 규칙 X / 부모가 없는 노드가 전체의 루트 노드
    parent = list(range(E+2))
    child_1 = [0] * (E+2)
    child_2 = [0] * (E+2)

    for i in range(E):
        if child_1[arr[2*i]] == 0:
            child_1[arr[2*i]] = arr[2*i + 1]
        else:
            child_2[arr[2*i]] = arr[2*i + 1]

    visited = [0] * (E + 2)
    def DFS(E, start, visited): # 간선의 개수 / 루트 노드
        visited[start] = 1

        if child_1[start]:
            next = child_1[start]
            DFS(E, next, visited)
        if child_2[start]:
            next = child_2[start]
            DFS(E, next, visited)

    DFS(E, N, visited)

    result = 0
    for i in range(1, E+2):
        if visited[i] == 1:
            result += 1
    print(f'#{test_case} {result}')
