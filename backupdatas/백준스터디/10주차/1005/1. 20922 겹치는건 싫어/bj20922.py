# 백준 20922. 겹치는 건 싫어
import sys
sys.stdin = open("bj20922input.txt")
from collections import deque, defaultdict

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    max_num = max(arr)

    num_count = [0 for _ in range(max_num+1)]
    que = deque()
    result = 0
    # 각 연속 부분 수열의 길이
    max_result = 0
    for i in range(N):
        num = arr[i]
        # 아직 추가 안했는데 K를 넘어버림,,,
        if num_count[num] == K:
            max_result = max(max_result, result)
            while True:
                n = que.popleft()
                num_count[n] -= 1
                result -= 1
                if n == num:
                    break
        que.append(num)
        num_count[num] += 1
        result += 1

    print(max(max_result, result))
