# 백준 2668. 숫자고르기
import sys
sys.stdin = open("bj2668input.txt")


input = sys.stdin.readline

N = int(input())

# 1번 ~
adj = [[] for _ in range(N + 1)]

# i번과 이어진 값들
for i in range(1, N + 1):
    adj[i].append(int(input()))

def dfs(num):
    if visited[num] == 0:
        visited[num] = 1
        for i in adj[num]:
            up.add(num)
            bottom.add(i)

            if up == bottom:
                result.extend(list(bottom))
                return

            dfs(i)
    visited[num] = 0

result = []
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    up = set()
    bottom = set()
    dfs(i)

result = list(set(result))
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])