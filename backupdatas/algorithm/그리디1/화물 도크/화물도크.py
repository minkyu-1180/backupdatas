# sw academy 화물 도크
import sys
sys.stdin = open("화물도크input.txt")


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x: x[1], reverse = True) # 각 작업의 끝나는 시간 기준 내림차순

    result = 0
    now_start, now_end = arr.pop()
    result += 1
    while arr:
        next_start, next_end = arr.pop()
        if now_end <= next_start: # 현재 작업중인 업무가 마치고 나서 시작할 경우
            now_end = next_end
            result += 1
    print(f'#{test_case} {result}')