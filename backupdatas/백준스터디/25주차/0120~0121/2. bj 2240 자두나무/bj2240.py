# 백준 2240. 자두나무
import sys
sys.stdin = open("bj2240input.txt")



# T : 자두가 떨어지는 총 시간(1 <= T <= 1000)
# W : 자두가 움직이고 싶어하는 횟수(1 <= W <= 30)
T, W = map(int, input().split())
'''
자두는 열매가 떨어지는 순간, 자두가 그 나무의 아래에 서 있으면 자두는 그 열매를 받아먹을 수 있음
- 자두는 하나의 나무 아래에 서 있다가 다른 나무 아래로 빠르게 움직일 수 있따
- 시작 : 1번 자두나무
'''

arr = []
for _ in range(T):
    # arr[i] : (i+1)초에 떨어지는 자두가 달려있는 나무 번호(1 or 2)
    arr.append(int(input()))
arr = [0] + arr
# 자두가 떨어지는 나무 위치가 바뀔 떄 옮길 것인가?? -> 옮기면 w가 늘어남
# 백트래킹으로 하기에는 T가 너무 커짐(2**1000)

# dp[t][w] : t초에 w번 움직였을 때의 최대 개수
dp = [[0] * (W+1) for _ in range(T+1)]

for t in range(1, T+1):
    # 0번 바뀜 -> t초에도 계속 1번에 위치하는 상태에서 하나 더 먹음
    if arr[t] == 1:
        dp[t][0] = dp[t-1][0] + 1
    elif arr[t] == 2:
        dp[t][0] = dp[t-1][0]

    for w in range(1, W+1):
        # 1번에 있음 + 지금 1번 or 2번에 있음 + 지금 2번
        if (arr[t] == 1 and w%2 == 0) or (arr[t] == 2 and w%2 == 1):
            dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])
            dp[t][w] += 1
        else:
            dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])

result = 0
for w in range(W+1):
    if result < dp[T][w]:
        result = dp[T][w]
print(result)