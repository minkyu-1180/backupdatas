# sw academy 컨테이너 운반
import sys
sys.stdin = open("컨테이너운반input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 컨테이너 수
    # M : 화물 수
    N, M = map(int, input().split())
    arr_cont = list(map(int, input().split()))
    arr_truck = list(map(int, input().split()))
    arr_cont.sort(reverse = True)
    arr_truck.sort()
    result = 0
    while arr_truck:
        truck = arr_truck.pop()
        for i in range(len(arr_cont)):
            if truck >= arr_cont[i]:
                result += arr_cont[i]
                arr_cont.pop(i)
                break
        if arr_cont == []:
            break

    print(f'#{test_case} {result}')