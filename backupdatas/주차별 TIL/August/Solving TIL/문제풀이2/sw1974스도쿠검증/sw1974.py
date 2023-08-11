# sw academy 문제풀이 2 - 1974. 스도쿠 검증
'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

[제약 사항]
1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
import sys
sys.stdin = open("sw1974input.txt")


# 9 x 9이 스도쿠인지 확인해주는 함수 정의
def issudoku(arr):
    # 행에 대한 확인
    for i in range(9):
        # i번 idx의 요소 : 해당 행/열에 포함된 i의 개수
        # 스도쿠는 1 ~ 9까지 모두 1이어야 함
        cnt_row = [0] * 10
        for j in range(9):
            cnt_row[arr[i][j]] += 1
        # 0번 idx는 볼 필요 X
        for k in range(1, 10):
            # 비어있는 숫자가 있을 경우, 0 반환
            # 즉, 함수를 호출할 때 0이 반환될 경우 not sudoku
            if cnt_row[k] == 0:
                return 0

    # 열에 대한 확인
    for j in range(9):
        cnt_col = [0] * 10
        for i in range(9):
            cnt_col[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt_col[k] == 0:
                return 0

    # 3 x 3 확인
    # 행과 열의 시작점 : 0, 3, 6
    # 주어진 (i, j) 쌍을 기준으로 움직일 수 있는 방법
    di = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dj = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    # i와 j 고정(0, 0), (0, 3), (0, 6), ,,, , (6, 6)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # idx의 값 : 현재 3x3 안에 들어있는 idx번호의 개수
            cnt_triple = [0] * 10
            for k in range(9):
                ni = i + di[k]
                nj = j + dj[k]
                cnt_triple[arr[ni][nj]] += 1
            for idx in range(1, 10):
                # 중복 원소가 존재하여 비어있는 숫자가 있을 경우
                if cnt_triple[idx] == 0:
                    return 0
    # 위의 경우를 다 통과한 경우 스도쿠 검증 완료
    return 1




# 테스트 케이스의 개수 T
T = int(input())
for test_case in range(1, T+1):
    # 9 x 9 퍼즐의 데이터
    arr = [list(map(int, input().split())) for _ in range(9)]
    # print(arr)

    print(f'#{test_case} {issudoku(arr)}')



'''
    # 행 탐색
    for i in range(9):
        # i번 index에 저장된 리스트를 set으로 형변환하여 저장
        temp = set(arr[i])
        # set의 길이가 9가 아닐 경우 즉, 중복된 원소가 제거된 경우
        # 더이상 살펴볼 필요가 없기 때문에 result 갱신 후 break을 통해 for문을 빠져나옴
        if len(temp) != 9:
            result = 0
            break
    # 열 탐색
    # 위의 for문에 의해 break가 되지 않은 경우(행에 대해서는 문제가 없는 경우) 진행
    if result == 1:
        # 특정 열 기준
        for j in range(9):
            # j열의 모든 행 원소들을 담는 방법 : append()
            temp = set()
            for i in range(9):
                # 새롭게 탐색중인 원소가 이미 temp에 들어가있는 경우
                # 즉, 중복 원소가 발생한 경우 -> result 갱신 후 종료
                if arr[i][j] in temp:
                    result = 0
                    break
                # 아직 temp에 들어가지 않은 경우 원소 추가
                else:
                    temp.append(arr[i][j])

    # 3 x 3 매트릭스 탐색
    # 위의 두 개의 for문에 의해 break가 되지 않은 경우(행과 열에 대해 문제가 없는 경우) 진행
    if result == 1:
        # 3 x 3 : (0,0) ~ (2,2), (3,3) ~ (2,2), .... , (6,6) ~ (8,8)
        temp = set()
        for i in range(0, 9, 3): # 0, 3, 6
            for j in range(0, 9, 3): # 0, 3, 6
'''







