# 백준 3078. 좋은 친구
import sys
sys.stdin = open("bj3078input.txt")
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, K = map(int, input().rstrip().split())
    counts = [0] * 21
    que = deque([])
    result = 0
    for i in range(N):
        name = len(input().rstrip())
        if i > K:
            popped = que.popleft()
            counts[popped] -= 1
        result += counts[name]
        que.append(name)
        counts[name] += 1
    print(result)