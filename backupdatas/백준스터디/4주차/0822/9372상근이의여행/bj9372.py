# 백준 9327. 상근이의 여행
import sys
sys.stdin = open("9372input.txt")

def DFS(start):
    global cnt
    visited[start] = 1
    for next in graph[start]:
        if visited[next] == 0:
            cnt += 1
            DFS(next)
    return cnt

T = int(input())
for test_case in range(1, T+1):
    # N : 국가 수 (2 <= N <= 1000)
    # M : 비행기 종류 (1 <= M <= 10000)
    N, M = map(int, input().split())
    '''
    M개의 줄 동안 a와 b쌍 입력
    a와 b를 왕복하는 비행기 존재
    최대한 적은 종류의 비행기를 타고 모든 국가 여행
    '''

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    nation = list(range(1, N+1))
    visited = [0] * (N+1)
    cnt = 0
    print(DFS(1))
