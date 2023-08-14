# 백준 17952. 과제는 끝나지 않아!
import sys
sys.stdin = open("17952input.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 총 점수
    result = 0
    # 현재 지난 시간(분 단위)
    time = 0
    score_stack = []
    time_stack = []
    while time < N:
        # 과제가 부여된 경우
        if arr[time][0] == 1:
            # 점수스택에 추가할 요소 : 점수
            score_stack.append(arr[time][1])
            time_left = arr[time][2]
            # 바로 과제를 시작했기 때문에 1분 감소
            time_left -= 1
            # 받자마자 과제를 끝낸 경우(1분짜리 과제)
            if time_left == 0:
                result += score_stack.pop()
            # 받자마자 1분동안 과제를 했음에도 아직 못 끝낸 경우
            else:
                # 타임스택에 추가할 요소 : 남은 시간
                time_stack.append(time_left)
        # 앞서 받은 과제를 추가로 해도 되는 경우
        else:
            if time_stack and score_stack:
                # 현재 하고 있는 과제의 남은 시간 감소
                time_stack[-1] -= 1
                # 해당 과제를 다 끝낸 경우
                if time_stack[-1] == 0:
                    time_stack.pop()
                    result += score_stack.pop()
            # 위의 과정을 진행한 경우 시간 증가
        time += 1

    print(result)



