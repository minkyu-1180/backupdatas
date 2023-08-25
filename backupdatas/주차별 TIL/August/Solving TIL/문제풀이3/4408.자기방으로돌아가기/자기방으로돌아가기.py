# 자기 방으로 돌아가기
import sys
sys.stdin = open("자기방으로돌아가기input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 돌아가야 할 학생들의 수
    '''
    홀수번호 : 위쪽 벽
    짝수번호 : 아래쪽 벽
    돌아가는 과정에 겹치는 복도구간이 있을 시, 한 사람은 기다렸다가 다음 차례에 이동
    거리에 관계없이 단위 시간이 걸림
    
    복도 번호 = (방 번호 + 방 번호 % 2) // 2
    홀수방 : 1 3 5 ..... 399
    복  도 : 1 2 3 ..... 200
    짝수방 : 2 4 6 ..... 400
    '''
    # [now, go]를 원소로 가지는 배열
    # now : 현재 방 번호
    # go : 가야 할 방 번호
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 복도(짝수 / 홀수 방 사이 공간을 지나는 사람 수를 저장)
    bokdo = [0] * 201
    for now, go in arr:
        # 방 번호 -> 복도 번호
        now = (now + now%2)//2
        go = (go + go%2)//2
        for i in range(min(now, go), max(now, go)+1):
            bokdo[i] += 1
    print(f'#{test_case} {max(bokdo)}')
