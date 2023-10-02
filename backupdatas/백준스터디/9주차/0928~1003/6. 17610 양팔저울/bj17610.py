# 백준 17610. 양팔저울
import sys
sys.stdin = open("bj17610input.txt")
input = sys.stdin.readline


def backtracking(idx, plus, minus):
    if idx == K:
        check = abs(plus - minus)
        if visited[check] == 0:
            visited[abs(plus - minus)] = 1
        return

    backtracking(idx + 1, plus + arr[idx], minus)
    backtracking(idx + 1, plus, minus + arr[idx])
    backtracking(idx + 1, plus, minus)


K = int(input())
arr = list(map(int, input().split()))
S = sum(arr)
visited = [0] * (S + 1)
backtracking(0, 0, 0)
result = visited.count(0)
print(result)