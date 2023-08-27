# IM 대비 12. 백준 2839 설탕배달
import sys
sys.stdin = open("2839설탕배달input.txt")

T = int(input()) # 제출시 빼고
for test_case in range(1, T+1):
    N = int(input()) # 총 설탕 수
    result = 0
    while N > 0:
        if N % 5 == 0:
            result += N//5
            N = N - ((N//5) * 5)
        else:
            N = N - 3
            result += 1
    # 위의 while문 종료 후에 설탕이 남은 경우(나누기 불가)
    if N != 0:
        result = -1
    print(result)