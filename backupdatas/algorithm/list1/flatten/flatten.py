# sw문제해결 기본 1일차 - Flatten
import sys
sys.stdin = open("flatteninput.txt")

for test_case in range(1, 11):
    # 덤프 횟수(옮기는 제한 횟수)
    N = int(input())
    # 100개의 요소(각 요소 : 상자의 높이)로 이루어진 배열
    arr = list(map(int, input().split()))
    # 현재 최고 높이와 최저 높이, 덤프 횟수 초기화
    min_val = max_val = arr[0]
    min_idx = max_idx = 0
    c = 0

    # max_val, min_val(최대 최소 층) / max_idx, min_idx(최대, 최소 층의 값이 있는 index) 설정
    for i in range(100):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    # 종료 조건 : 총 N번의 덤프를 시행했을 경우
    # 최고층의 상자 -> 최저층의 상자
    # count += 1 & 다시 최고층과 최저층 설정
    while c < N:
        # 덤프 1회 시행
        c += 1
        max_val -= 1
        min_val += 1
        arr[max_idx] -= 1
        arr[min_idx] += 1

        # 중간 break 조건
        if max_val - min_val <= 1:
            break
        # 최고, 최저 높이 갱신(변화로 인해 바꼈을수도)
        for i in range(100):
            if arr[i] > max_val:
                max_val = arr[i]
                max_idx = i
            if arr[i] < min_val:
                min_val = arr[i]
                min_idx = i
        # 갱신된 높이의 차이가 1보다 작거나 같을경우

    # while문에서 빠져나온 경우
    # 즉, 제한 횟수만에 높이차가 1보다 작거나 같아지지 않은 경우
    result = max_val - min_val
    print(f'#{test_case} {result}')
