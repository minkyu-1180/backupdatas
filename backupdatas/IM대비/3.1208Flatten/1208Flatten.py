# IM 대비 3. Flatten
import sys
sys.stdin = open("Flatteninput.txt")

T = 10
for test_case in range(1, T+1):
    N = int(input()) # 덤프 횟수(1 <= N <= 1000)

    # 각 idx의 상자 높이
    arr = list(map(int, input().split()))

    # 최대값 , 최소값의 idx 초기값 설정
    max_i = min_i = 0
    for i in range(1, len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
        if arr[min_i] > arr[i]:
            min_i = i


    dump = 0 # 덤프 시행 횟수
    while dump < N: # 덤프 시행횟수가 N이 되는 순간 종료
        dump += 1

        # 리스트 요소 할당값과 해당 요소를 저장한 변수는 연산이 연결되지 않음
        # 원본 배열에도 적용
        arr[max_i] -= 1
        arr[min_i] += 1

        if arr[max_i] - arr[min_i] <= 1:
            break
        # break에 걸리지 않은 경우 최대/최소 idx 갱신
        for i in range(len(arr)):
            if arr[max_i] < arr[i]:
                max_i = i

            if arr[min_i] > arr[i]:
                min_i = i
    result = arr[max_i] - arr[min_i]
    print(f'#{test_case} {result}')
