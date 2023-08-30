# 백준 12852. 1로 만들기 2
import sys
from collections import deque
sys.stdin = open("12852input.txt")


'''
dfs는 시간초과가 나네...
def dfs(N, min_v):
    visited = [0] * (N+1)
    visited[1] = 1
    stack = []
    start = 1
    while True:
        if start == N and visited[start] - 1 == min_v:
            stack.append(N)
            break

        for next in (start * 3, start * 2, start + 1):
            if next <= N and visited[next] != visited[start] + 1:
                stack.append(start)
                visited[next] = visited[start] + 1
                start = next
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break

    return stack
'''


'''
T = int(input())
for tc in range(T):
    N = int(input())
    que = deque()
    que.append([N]) # 그냥 que = deque([N])를 하면 왠지 모르게 now 정의시 int형은 인덱싱/슬라이싱 불가 멘트가 뜸

    while que:
        lst = que.popleft()
        now = lst[-1]
        if now == 1:
            break
        if now % 2 == 0:
            que.append(lst + [now // 2])
        if now % 3 == 0:
            que.append(lst + [now // 3])
        que.append(lst + [now - 1])
    print(len(lst)-1)
    print(*lst)
'''

T = int(input())
for tc in range(T):
    N = int(input())

    dp = [[0, []] for _ in range(N+1)]
    # dp의 i번째 :
    # dp[i][0] : 최소연산횟수
    # dp[i][1] : 연산과정
    dp[1][0], dp[1][1] = 0, [1]
    for i in range(2, N+1):
        # 1인 경우
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = dp[i-1][1] + [i]

        # 2로 나누어 떨어지는 경우
        if i%2 == 0:
            if dp[i][0] > dp[i//2][0] + 1:
                dp[i][0] = dp[i//2][0] + 1
                dp[i][1] = dp[i//2][1] + [i]
        if i%3 == 0:
            if dp[i][0] > dp[i//3][0] + 1:
                dp[i][0] = dp[i // 3][0] + 1
                dp[i][1] = dp[i // 3][1] + [i]

    print(dp[N][0])
    for i in dp[N][1][::-1]:
        print(i, end = ' ')
    print()