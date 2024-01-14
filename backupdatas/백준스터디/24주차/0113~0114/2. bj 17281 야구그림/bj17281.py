# 백준 17281. 야구그림
import sys
from itertools import permutations
sys.stdin = open("bj17281input.txt")
input = sys.stdin.readline

def hit_result(now_base, now_hit):
    cnt = 0
    base = [0] * 4
    # 안타
    # 타석 -> 1루 / 1루 -> 2루 / 2루 -> 3루 / 3루 -> 점수
    if now_hit == 1:
        cnt = now_base[3]
        base = [0, 1, now_base[1], now_base[2]]
    # 2루타
    # 타석 -> 2루 / 1루 - > 3루 / 2, 3루 -> 점수
    elif now_hit == 2:
        cnt = now_base[3] + now_base[2]
        base = [0, 0, 1, now_base[1]]
    # 3루타
    # 타석 -> 3루 / 1, 2, 3루 -> 점수
    elif now_hit == 3:
        cnt = now_base[3] + now_base[2] + now_base[1]
        base = [0, 0, 0, 1]
    # 홈런
    # 1, 2, 3루 + 본인 -> 점수
    else:
        cnt = sum(now_base) + 1

    return cnt, base

def inning(per):
    # 1번 선수는 무조건 4번 타자 고정
    now_inning = list(per[:3]) + [0] + list(per[3:])
    now_cnt = 0
    # 현재 타자 번호
    now = 0
    # i+1 번 이닝 상황 보기
    for i in range(N):
        out_c = 0
        # now_base[i] : i+1번 베이스에 진출 유무
        now_base = [0] * 4

        while out_c < 3:
            # 현재 마운트에 올라온 타자가 현재 이닝에서 몇 점을 칠까?
            now_hit = arr[i][now_inning[now]]

            if now_hit == 0:
                out_c += 1
            else:
                cnt, now_base = hit_result(now_base, now_hit)
                now_cnt += cnt
            # 다음 타자
            now = (now+1) % 9
    return now_cnt

T = int(input())
for tc in range(T):

    # N : 이닝 수(2 <= N <= 50)
    N = int(input().rstrip())

    # arr[i][j] : (i+1)번 이닝에서 (j+1)번 타자의 결과
    '''
    안타 : 1
    2루타 : 2
    3루타 : 3
    홈런 : 4
    아웃 : 0
    '''
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
    # print(arr)
    '''   
    1번 선수가 무조건 4번 타자
    -> 1번 ~ 3번타자 + 4번 타자(1) + 5번 ~ 9번 타자
    아웃(0)이 3번 -> 공수교대
    '''
    result = 0
    for case in permutations(range(1, 9), 8):
        case_now = list(case[:3]) + [0] + list(case[3:])

        now_hit = 0
        now_cnt = 0

        for i in range(N):
            out_c = 0
            b1 = b2 = b3 = 0
            while out_c < 3:
                point = arr[i][case_now[now_hit]]
                if point == 0:
                    out_c += 1
                else:
                    if point == 1:
                        now_cnt += b3
                        b1, b2, b3 = 1, b1, b2
                    elif point == 2:
                        now_cnt += (b2 + b3)
                        b1, b2, b3 = 0, 1, b1
                    elif point == 3:
                        now_cnt += (b1 + b2 + b3)
                        b1, b2, b3 = 0, 0, 1
                    else:
                        now_cnt += (1 + b1 + b2 + b3)
                        b1 = b2 = b3 = 0
                now_hit = (now_hit+1) % 9
        if result < now_cnt:
            result = now_cnt

        # print(case_now)
        # # print(per)
        # c = inning(per)
        # if result < c:
        #     result = c
    print(result)

