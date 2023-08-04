# 2578. 빙고
import sys
sys.stdin = open("2578input.txt")

# 빙고판에 쓰여진 수(5 X 5)
my_bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 불러주는 순서
num_seq = [list(map(int, input().split())) for _ in range(5)]
new_seq = []

# 사회자가 불러주는 순서를 1차원 배열에 할당
for i in range(5):
    for j in range(5):
        new_seq.append(num_seq[i][j])

# 불러주는 순서대로 (i, j)th idx에 1을 넣을 결과판
result = [[0] * 5 for _ in range(5)]

# 사회자가 부른 숫자 개수
n = 0
# 다 채워진 행 / 열 / 대각선의 횟수
count = 0
while n < 25:
    # while문을 한 바퀴 돌았을 때 count(모든 줄이 1인 열 / 행 / 대각선의 개수 합)이 3보다 크거나 같을 경우
    if count >= 3:
        # while문에서 빠져나감
        break

    # n+1번째 불러준 숫자
    num = new_seq[n]
    for i in range(5):
        for j in range(5):
            if my_bingo[i][j] == num:
                result[i][j] = 1
                n += 1
                # 숫자를 부른 후 result의 i번 row / j번 col
                ith_row = [result[i][l] for l in range(5)]
                jth_col = [result[k][j] for k in range(5)]

                # 해당 row가 [1, 1, 1, 1, 1]일 경우
                if ith_row == [1] * 5:
                    count += 1
                # 해당 col이 [1, 1, 1, 1, 1]일 경우
                if jth_col == [1] * 5:
                    count += 1
                # 우측 아래로 향하는 대각선 존재
                if i == j:
                    down_diag = [result[k][k] for k in range(5)]
                    if down_diag == [1] * 5:
                        count += 1

                # 우측 위로 향하는 대각선 존재
                if i + j == 4:
                    up_diag = [result[k][4-k] for k in range(5)]
                    if up_diag == [1] * 5:
                        count += 1

print(n)