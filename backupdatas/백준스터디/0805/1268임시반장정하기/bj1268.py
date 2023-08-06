# 1268. 임시 반장 정하기
import sys
sys.stdin = open("1268input.txt")

# 학생 수
N = int(input())
# 행 : 학생 번호 - 1 / 열 : 학년 번호 - 1
arr = [list(map(int, input().split())) for _ in range(N)]

# result[i][j] : (i+1) 번 학생과 (j+1)번 학생이 같은 반을 한 경험 유무
result = [[0] * N for _ in range(N)]

# 각 학년 별(j : 학년 - 1)
for j in range(5):
    # 각 학생 번호(i : 번호 - 1)
    for i in range(N-1):
        # i번 index의 학생과 비교할 학생 번호(k : 번호 - 1)
        for k in range(i+1, N):
            # 해당 학년 때 같은 반이 한 적 있으면 1 할당
            if arr[i][j] == arr[k][j]:
                result[i][k] = result[k][i] = 1

# 최대 횟수
max_c = 0
# 최대 횟수를 가진 학생 번호
std_num = 0
for i in range(N):
    # (i+1)번 학생의 같은 반을 해본 학생 수
    same_c = result[i].count(1)
    # 작은 번호만 출력(같은게 아니라 커야만 max값이 바뀜)
    if same_c > max_c:
        max_c = same_c
        # 원하는 결과(학생 번호)
        std_num = i + 1

print(std_num)