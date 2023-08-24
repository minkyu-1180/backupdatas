# IM 대비 7. 민석이의 과제 체크하기
import sys
sys.stdin = open("과제체크input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 총 학생 수(학생 번호 : 1 ~ N) / 2 <= N <= 100
    # K : 과제 제출 학생 수(1 <= K <= N)
    N, K = map(int, input().split())

    # 과제 제출 목록
    hw_done = list(map(int, input().split()))

    print(f'#{test_case}', end = ' ')
    for std in range(1, N+1): # std : 학생 번호(오름차순으로 반복문 실행)
        if std not in hw_done:
            print(std, end = ' ')
    print()


