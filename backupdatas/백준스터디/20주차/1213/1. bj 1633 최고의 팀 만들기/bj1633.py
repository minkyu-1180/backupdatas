# 백준 1633. 최고의 팀 만들기
import sys
sys.stdin = open("bj1633input.txt")

# 입력 list : 백으로 플레이할 때 능력치, 흑으로 플레이할 때 능력치
# 무한 입력 처리 방식
# dp[i][j] : 백플레이어를 i명, 흑플레이어를 j명 골랐을 때의 능력치 최대
# dp[i-1][j] : 백플레이어를 i-1명, 흑플레이어를 j명 골랐을 때의 능력치 최대
'''
87 84 
dp[0][1] = 84
dp[1][0] = 87

66 78
dp[0][2] = 162
dp[1][1] = max(dp[0][1] + 66, dp[1][0] + 78) = 165
dp[2][0] = 153
'''
# dp = [[0] * 16 for _ in range(16)]

arr = []
dp = [[[0] * 16 for _ in range(16)] for _ in range(1001)]
while True:
    try:
        w, b = map(int, input().split())
        arr.append((w, b))
    except:
        N = len(arr)
        # 각 층별로 dp 갱신
        # 현재 선택한 명 수
        for n in range(1, N+1):
            # 현재 사람의 능력치
            w, b = arr[n-1]
            # dp[n][i][j] : n명 중, 백이 i명, 흑이 j명일 때 최대 값
            # dp[n-1][i-1][j] : n-1명 중 백이 i-1, 흑이 j명일 때 최대 값
            # dp[n-1][i][j-1] : n-1명 중 백이 i, 흑이 j명일 때 최대 값
            # -> n-1인 상태에서 n명인 상태가 되었을 때 값을 갱신
            for i in range(16):
                for j in range(16):
                    if i + j <= n:
                        # 현재 사람을 n명 안에 포함 안 시킬 경우
                        dp[n][i][j] = max(dp[n][i][j], dp[n-1][i][j])

                        # 백 추가 가능
                        if i > 0:
                            dp[n][i][j] = max(dp[n][i][j], dp[n-1][i-1][j] + w)
                        # 흑 추가 가능
                        if j > 0:
                            dp[n][i][j] = max(dp[n][i][j], dp[n-1][i][j-1] + b)

            # for i in dp[n]:
            #     print(i)
        print(dp[N][15][15])
        break