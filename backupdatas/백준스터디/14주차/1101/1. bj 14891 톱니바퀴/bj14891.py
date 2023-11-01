# 백준 14891. 톱니바퀴
import sys
sys.stdin = open("bj14891input.txt")


# 원래 T는 없음
T = int(input())
for tc in range(T):
    arr = [[]]
    # status[i] : i번 톱니바퀴가 현재 12시 방향을 가리키는 인덱스 번호
    # 초기값 : 모두 0번 인덱스가 현재 12시를 가리키는 중
    status = [0] * 5
    # 톱니바퀴 초초 상태 넣기
    # 12시 방향부터 시계방향 순으로(N극 : 0, S극 : 1)
    for i in range(1, 5):
        arr.append(list(map(int, input())))
    # print(arr)
    # print(status)

    # 회전 횟수(1 <= K <= 100)
    K = int(input())
    for _ in range(K):
        # number : 회전시킬 톱니바퀴 번호
        # direction : 방향(1 : 시계방향, -1 : 반시계 방향)
        num, dir = map(int, input().split())

        # # 현재 기준이 되는 톱니바퀴의 2번(오른쪽), 6번(왼쪽)의 극
        # num_r = (status[num]+2)%8
        # num_l = (status[num]+6)%8

        # left_r : 왼쪽 방향으로 가는 기준 인덱스(left_l을 left_r 로부터 구해서 확인)
        # right_l : 오른쪽 방향으로 가는 기준 인덱스(right_r을 right_l 로부터 구해서 확인)
        left_r = right_l = num
        left_l = left_r - 1
        right_r = right_l + 1

        # d_l : left_r의 direction
        # d_r : right_l의 direction
        d_l = d_r = dir

        # directions[i] : i번 톱니바퀴의 회전 방향(1 : 시계 / -1 : 반시계 / 0 : 그대로)
        directions = [0] * 5
        directions[num] = dir # 초기값 설정

        # while문 안에서 둘 다 False가 되면 멈추기(더이상 왼쪽/오른쪽 진행 불가)
        left_flag = right_flag = True
        while 1 <= left_l or right_r <= 4:
            # break 조건
            if left_flag == False and right_flag == False:
                break
            # 왼쪽에 톱니바퀴 존재 & 돌리기 가능
            # arr[left_l][(status[left_l]+2)%8]의 의미
            # : left_l번 톱니바퀴에서 현재 3시 방향을 가리키는 인덱스 번호
            # 만약 left_l번 톱니바퀴가 없거나, left_l번 톱니바퀴의 3시 방향 인덱스 != left_r번 톱니바퀴의 9시 방향 인덱스이면
            # 더이상 갈 필요 X(left_r까지만 direction이 정해짐)
            if 1 > left_l or arr[left_l][(status[left_l] + 2) % 8] == arr[left_r][(status[left_r] + 6) % 8]:
                left_flag = False

            # 위에서 left_flag가 False가 되지 않은 경우 -> left_l번 톱니바퀴의 회전 방향 정하고 그 왼쪽 보기
            if left_flag:
                directions[left_l] = directions[left_r] * -1
                left_l -= 1
                left_r -= 1

            # 오른쪽도 마찬가지
            if right_r > 4 or arr[right_r][(status[right_r] + 6) % 8] == arr[right_l][(status[right_l] + 2) % 8]:
                right_flag = False
            if right_flag:
                directions[right_r] = directions[right_l] * -1
                right_l += 1
                right_r += 1

        # while문이 끝난 경우 -> direction과 status 이용
        for i in range(1, 5):
            if directions[i] == -1:
                status[i] = (status[i] + 1)%8
            elif directions[i] == 1:
                if status[i] == 0:
                    status[i] = 7
                else:
                    status[i] -= 1

    # print(status)
    result = 0
    for i in range(1, 5):
        idx = status[i]

        if arr[i][idx] == 1:
            result += 2**(i-1)
    print(result)




