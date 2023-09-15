# 백준 7682. 틱택토
import sys
sys.stdin = open("bj7682input.txt")

# 해당 플레이어가 빙고를 만들어 내는가?
# player : X or O
# idx1, idx2, idx3 : 주어진 문자열(길이 9) 내에서 빙고를 만들어낼 수 있는 인덱스 조합
def bingo(player, idx1, idx2, idx3):
    if arr[idx1] == arr[idx2] == arr[idx3] == player:
        return True

    return False

# 현재 배열 기준으로 valid가 가능한가요?
def isvalid(arr):
    # 배열 내의 X와 O의 개수
    X_s = arr.count('X')
    O_s = arr.count('O')
    # X가 빙고가 되는 횟수 / O가 빙고가 되는 횟수
    X_bingo_count = 0
    O_bingo_count = 0

    # 우선 최대한 빙고가 나올 환경을 만들었습니다.
    if X_s >= 3: # X가 최소 O보다 적지는 않아야 함 -> 최소 케이스(X : 3, O : 2개 and X가 빙고)
        # X가 이기는 케이스 최소 조건
        if X_s - O_s == 1:
            # 모든 빙고 확인 인덱스 조합에 대해, X가 만들어내는 빙고와 O가 만들어내는 빙고의 개수 세기
            for i1, i2, i3 in bingo_case:
                if arr[i1] == 'X' and bingo('X', i1, i2, i3):
                    X_bingo_count += 1
                elif arr[i1] == 'O' and bingo('O', i1, i2, i3):
                    O_bingo_count += 1
            # 무조건 X가 이겨야 함 -> O의 빙고 개수는 0이고 X의 빙고 개수는 최소 1개
            if (X_bingo_count >= 1) and (O_bingo_count == 0):
                return True
            # 만약 둘 다 이기지 못한 경우 -> 꽉 찰 때까지 빙고가 없는 케이스밖에 안됨
            elif (X_bingo_count == O_bingo_count == 0) and ('.' not in arr):
                return True

        # O가 이기는 케이스 최소 조건(이 경우는 꽉 찰 때 까지 가질 않아요)
        elif X_s - O_s == 0:
            for i1, i2, i3 in bingo_case:
                if bingo('X', i1, i2, i3):
                    X_bingo_count += 1
                if bingo('O', i1, i2, i3):
                    O_bingo_count += 1
            # 무조건 O가 이겨야 함 -> O의 빙고 개수는 최소 1개 and X의 빙고 개수는 0개
            if X_bingo_count == 0 and O_bingo_count >= 1:
                return True

    # 위의 케이스에서 return 되지 않은 경우는 False
    return False


bingo_case = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
              (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

arr = list(input())
while True:

    if len(arr) == 3:
        break

    for i in range(9):
        # 빈 공간이 아닐 경우
        if arr[i] != '.':
            # 현재 자리 미리 저장 후, 그 전 상태로 되돌려서 그 전에는 invalid가 나왔는지 먼저 확인
            real_i = arr[i]
            arr[i] = '.'
            result_1 = isvalid(arr)
            arr[i] = real_i # 다시 원래 상황으로 돌려줘
            if not result_1: # 그 전 상황이 False야? 그러면 현재 상황이 True면 원하는 결과네?
                result_2 = isvalid(arr)
                if result_2:
                    print('valid')
                    break
    else:
        print('invalid')

    arr = list(input())

'''
    result = 'invalid'

    X_s = arr.count('X')
    O_s = arr.count('O')
    X_bingo_count = 0
    O_bingo_count = 0

    if X_s >= 3:
        # X가 이기는 케이스
        if X_s - O_s == 1:
            for i1, i2, i3 in bingo_case:
                if arr[i1] == 'X' and bingo('X', i1, i2, i3):
                    X_bingo_count += 1
                elif arr[i1] == 'O' and bingo('O', i1, i2, i3):
                    O_bingo_count += 1
            if X_bingo_count >= 1 and O_bingo_count == 0:
                result = 'valid'
            elif '.' not in arr:
                result = 'valid'
        
        # O가 이기는 케이스
        elif X_s - O_s == 0:
            for i1, i2, i3 in bingo_case:
                if bingo('X', i1, i2, i3):
                    X_bingo_count += 1
                if bingo('O', i1, i2, i3):
                    O_bingo_count += 1
            if X_bingo_count == 0 and O_bingo_count >= 1:
                result = 'valid'
'''