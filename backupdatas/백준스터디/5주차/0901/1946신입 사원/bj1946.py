# 백준 1946. 신입 사원
import sys
sys.stdin = open("1946input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key = lambda x : x[0])
    # print(arr)

    c = 1 # 서류 1등은 무조건 채용

    for i in range(1, N):
        score = arr[i]
        # 서류가 i번 지원자보다 높은 사람들과 비교
        for j in range(0, i):
            vs_score = arr[j]
            # i번 지원자가 j번 지원자보다 면접순위도 낮을 경우 탈락
            if score[1] > vs_score[1]:
                break
        # 서류성적이 본인보다 좋은 참가자들과 비교 시, 면접성적이라도 좋은 경우
        else:
            c += 1
    print(c)