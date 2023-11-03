# 백준 2660. 회장 뽑기
import sys
from collections import deque
sys.stdin = open("bj2660input.txt")

def bfs(i):
    # 본인 제외하고 나머지들과 다 친구관계를 맺기 위해 필요한 깊이 -> -1로 초기화
    visited = [-1] * (N+1)
    visited[i] = 0 # 본인은 0
    que = deque()
    que.append(i)
    check_cnt = 1 # 총 몇 명과 친구관계가 됨?(본인 제외 -> 1명 넣어두기)

    while que:
        now = que.popleft()
        for friend in arr[now]:
            if visited[friend] == -1:
                visited[friend] = visited[now] + 1
                check_cnt += 1
                # i번 사람이 모든 사람들과 친구 관계가 맺어진 순간, 해당 친구까지 도달하는 데 걸린 거리가 곧 결과값
                if check_cnt == N:
                    return visited[friend]
                # 아직 아니면 큐에 추가
                que.append(friend)

    # return max(visited)

# N : 회원의 수 (1 <= N <= 50)
N = int(input())
# arr[i][j] : i와 j는 친구
arr = [[] for _ in range(N+1)]

# 친구 관계 추가
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

# 결과값을 담을 배열
result = [0] * (N+1)
# 각 배열 별로 친구 관계를 맺기 위한 depth 넣기
for i in range(1, N+1):
    result[i] = bfs(i)

# 원하는 것 : 친구관계를 맺기 위한 depth의 최소값, 해당 최소값 만큼의 횟수를 진행한 사람들 명 수
min_v = min(result[1:])
print(min_v, result.count(min_v))

# 해당 사람들의 번호 출력
for i in range(1, N+1):
    if result[i] == min_v:
        print(i, end = ' ')
print()
