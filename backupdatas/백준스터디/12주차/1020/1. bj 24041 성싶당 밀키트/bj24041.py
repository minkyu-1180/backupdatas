# 백준 24041. 성싶당 밀키트
import sys
sys.stdin = open("bj24041input.txt")

# 원래 T는 없음
# T = int(input())
# for tc in range(T):
# N : 밀키트의 재료 개수(1 <= N <= 200000)
# G : 세균 수 기준(모든 재료의 세균수의 합이 <= G일 경우, 먹어도 됨)
# 1 <= G <= 10**9
# K : 최대 뺄 수 있는 재료(0 <= K < N)
N, G, K = map(int, input().split())
arr = []
min_day = 0
max_day = 2*int(1e9)
for _ in range(N):
    # S : i번째 재료의 부패 속토(1 <= S <= 10**9)
    # L : i번째 재료의 유통기한(일) (1 <= L <= 10**9)
    # 구매 후 x일에 i번째 재료의 세균수 : S X max(1, x-L)
    # O : 중요한 재료 여부(0 : 중요 / 1 : 중요 X -> 빼도 됨)
    S, L, O = map(int, input().split())
    arr.append([S, L, O])

# O == 0이 앞에 오게끔 정렬
arr.sort(key = lambda x : x[2])
# result = 0
# print(arr)
while min_day <= max_day:
    # 구매 후 지난 일 수
    mid = (min_day + max_day)//2
    counts = 0 # 안 넣은 재료 개수
    virus_sum = 0 # mid 일 후 총 바이러스 합(사용할 재료들의 바이러스 합)

    not_have_to = []
    for s, l, o in arr:
        virus = s * max(1, mid - l)
        if o == 0: # 반드시 넣어야 하는 재료일 경우
            # 재료를 포함시키고 바이러스 합 추가
            virus_sum += virus
        else: # 반드시 넣어야 하지는 않을 경우
            not_have_to.append(virus) # 배열에 mid 일째에 해당 재료로부터 증식한 바이러스 수 추가
    # 바이러스 개수들을 오름차순으로 정렬
    not_have_to.sort()

    V = len(not_have_to)
    for v in range(V):
        virus = not_have_to[v]
        # 해당 재료를 포함시키면 바이러스 개수가 넘침
        # 그럼 뒤에 재료들을 포함해도 넘치니까 멈추고, 남은 재료들의 개수가 곧 counts
        if virus_sum + virus > G:
            counts = V-v
            break
        # 추가해도 안넘치면 추가해주기
        else:
            virus_sum += virus

    if virus_sum > G:
        max_day = mid-1
    else:
        # G를 안넘도록 넣었을 때, 뺀 재료 개수 : V-v
        # 너무 많이 빼버림
        if counts > K:
            # 지난 일수를 줄임으로써, 뺀 재료를 줄여야징
            max_day = mid - 1
        # 더 빼도 되는 상황
        else:
            # if result < mid:
            #     result = mid
            # 지난 일수를 늘림으로써, 뺄 수 있는 재료를 늘려보자
            min_day = mid + 1
# 최대 며칠까지 버팅길 수 있는가?
print(max_day)