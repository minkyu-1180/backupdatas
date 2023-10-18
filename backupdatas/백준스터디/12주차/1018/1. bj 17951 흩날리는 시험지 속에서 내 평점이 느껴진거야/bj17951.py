# 백준 17951. 흔탈리는 시험지 속에서 내 평점이 느껴진거야
import sys
sys.stdin = open("bj17951input.txt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

min_score = min(arr)
max_score = sum(arr)

while min_score <= max_score:
    # 내가 정한 구간의 최소 점수 합
    mid = (min_score+max_score)//2
    c = 1 # 구간 개수

    i = 0
    score_sum = 0
    for j in range(i, N):
        # 이번 점수를 구간에 포함시켜도 최소값(mid)보다 작을 경우, 추가
        if score_sum + arr[j] < mid:
            score_sum += arr[j]
        # 최소값을 넘어갈 경우, 구간 추가 및 i 갱신
        else:
            c += 1
            i = j
            score_sum = 0
    # mid를 현재 받을 수 있는 그룹의 점수합 중 최소값으로 선정한 경우
    
    # 그룹이 K개보다 많아지면 -> min을 증가시켜 최소값을 넉넉하게
    if c > K:
        min_score = mid+1
    # 그룹이 K개보다 적어지면 -> max_를 감소시켜 최소값이 빡빡하게 
    elif c <= K:
        max_score = mid-1
# 최소 점수가 최대값이 될 경우 -> max_score 출력
print(max_score)
