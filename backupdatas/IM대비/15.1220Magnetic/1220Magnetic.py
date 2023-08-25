# IM 대비 15. Magnetic
import sys
sys.stdin = open("Magneticinput.txt")


for test_case in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0 # 교착상태 개수
    for j in range(100):
        N_wait = False # N극(1)이 들어올 경우, 하나만 넣어놓기 -> S극(2)가 오면 N의 대기상태 확인
        for i in range(100):
            if arr[i][j] == 1:
                if not N_wait:
                    N_wait = True
            elif arr[i][j] == 2:
                if N_wait: # 위에 N극이 있을 경우 -> 교착 발생
                    result += 1 # 교착횟수 갱신
                    N_wait = False  # 교착 발생한 N-S 관계 초기화

    print(f'#{test_case} {result}')