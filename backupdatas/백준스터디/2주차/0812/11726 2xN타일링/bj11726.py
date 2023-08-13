import sys
sys.stdin = open("11726input.txt")

def DP(N):
    global memo
    memo[1], memo[2] = 1, 2
    for i in range(3, N+1):
        memo[i] = (memo[i-1] + memo[i-2]) % 10007
    return memo[N]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # memoization을 사용할 경우, 최대 N값 + 1(1000 + 1)만큼의 크기를 생성
    memo = [0] * (1001)
    print(DP(N))