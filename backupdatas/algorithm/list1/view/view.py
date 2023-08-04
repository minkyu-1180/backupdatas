# sw문제해결 기본 1일차 - view
import sys
sys.stdin = open("viewinput.txt")

for test_case in range(1, 11):
    N = int(input())

    arr = list(map(int, input().split()))
    # 0, 0, [2], ,,, , [N-3], 0, 0
    counts = [0] * N
    for i in range(2, N-2):
        # i기준 i-2, i-1, i+1, i+2 번 index와 비교시 가장 높은 건물일 경우
        sub_max = 0
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            # i번 index 건물의 높이가 양 옆 두 채의 건물들보다 더 높음
            max = arr[i]
            # i번 index 건물의 조망권 세대 수
            c = 0
            for j in [i-2, i-1, i+1, i+2]:
                if arr[j] > sub_max:
                    sub_max = arr[j]
            c = max - sub_max
            counts[i] = c
    result = 0
    for i in counts:
        result += i
    print(f'#{test_case} {result}')


'''
result = 0
for i in range(2, N-2):
    # 현재 조사대상의 높이 : 최대 조망권
    tmp = arr[i]
    
    for j in range(i-2, i+3):
        # j가 자기자신일 경우는 비교 X
        if i == j:
            continue
        # 조사 대상의 양 옆보다 크면서 그들의 차이가 최대 조망권보다 작을 경우
        if arr[i] > arr[j] and tmp > arr[i] - arr[j]:
            tmp = arr[i] - arr[j]
        # 만약 조사 대상의 양 옆이 나와 크기가 같은 경우가 한번이라도 있을 경우
        # 더 이상 조사할 필요 X
        elif arr[i] <= arr[j]:
            break
        
        # break문으로 인해 종료되지 않은 경우(i가 아직 그대로)
        # 정상적으로 모두 조사가 끝난 경우
        else:
            # i번의 인덱스 위치 건물의 조망권 크기 더하기
            result += tmp
'''