# 백준 5567. 결혼식
import sys
sys.stdin = open("bj5567input.txt")
from collections import defaultdict, deque

def bfs():
    result = 0

    que = deque()
    visited = [0] * (N+1)
    que.append('1')
    visited[1] = 1

    while que:
        now = que.popleft()
        for next in dictionary[now]:
            if visited[int(next)] == 0 and (now =='1' or now in dictionary['1']):
                visited[int(next)] = 1
                que.append(next)
                result += 1
    return result

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 상근이의 동기 수(2 <= N <= 500)
    N = int(input())
    # M : 리스트의 길이(1 <= M <= 10000)
    M = int(input())
    # 친구 관계
    dictionary = defaultdict(list)
    for _ in range(M):
        a, b = map(str, input().split())
        dictionary[a].append(b)
        dictionary[b].append(a)
    print(bfs())