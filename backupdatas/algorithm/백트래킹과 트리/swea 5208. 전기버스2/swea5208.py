# swea 5208. 전기버스 2
import sys
sys.stdin = open("swea5208input.txt")

# 현재 자리 / 현재 횟수 / 현재 남은 충전량
def backtracking(idx, c, rest):
    global result

    # 남은 칸 수가 연료로 감당 가능하거나, 끝까지 다 확인했을 때
    if idx + rest == len(arr) or idx == len(arr):
        if result > c:
            result = c
        return

    # 기존 최소 교체횟수보다 크거나 같으면 더 할 필요 X(가지치기)
    if result > c:
        # 아직 남은 연료가 있을 경우, 현재 칸에서 교체 없이 연료 소모하여 넘어갈 수 있음
        if rest >= 1:
            backtracking(idx+1, c, rest-1)
        # 교체하는 경우
        backtracking(idx+1, c+1, arr[idx] - 1)

T = int(input())
for tc in range(1, T+1):
    # arr[0] : N
    # arr[1] ~ arr[N-1] : i번서 장착 가능한 충전지 용량
    arr = list(map(int, input().split()))
    # 최소한의 교환횟수를 출력하기
    # 출발지에서 배터리 장착은 교환횟수에 포함 X
    result = len(arr)

    # 1에서 2로 넘어가는데 연료를 이미 사용함(1번)
    backtracking(2, 0, arr[1]-1)

    print(f'#{tc} {result}')