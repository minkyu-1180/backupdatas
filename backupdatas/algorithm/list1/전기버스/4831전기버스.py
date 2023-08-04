# sw academy - 4831. 전기버스
import sys
sys.stdin = open("전기버스input.txt")


T = int(input())
for test_case in range(1, T + 1):
    # K :최대 이동 정류장 수 / N :종점 정류장 번호(0 ~ N번까지의 정류장) / M :충전기 개수
    K, N, M = map(int, input().split())
    # 충전기의 위치를 담을 배열
    arr = list(map(int, input().split()))

    # 시작 위치
    now_loc = 0
    after_k = now_loc + K
    # 충전을 할 주유소 위치
    charge = -1
    c = 0

    # 충전할 주유소 기준 k번의 뒷 정류장에 도달하면 종료
    while after_k < N:
        # 모든 주유소가 있는 정류장 위치의 인덱스에 대해 반복
        for i in range(len(arr)):
            # 현재 위치와 K만큼 떨어진 위치 사이에 주유소가 있는 경우 업데이트
            if now_loc < arr[i] <= after_k:
                charge = arr[i]
            # 주유소가 최대 버틸 수 있는 정류장보다 더 멀리 있는 경우
            elif after_k < arr[i]:
                break
        # 주유소 인덱스 위치가 -1 즉, 업데이트가 되지 않았을 경우
        # c를 0으로 두어 while문 종료
        if charge == -1:
            c = 0
            break
        # 위에서 문제가 없었을 경우, 현재 위치를 다시 해당 주유소 위치로 업데이트
        now_loc = charge
        after_k = now_loc + K
        c += 1
        charge = -1

    print(f'#{test_case} {c}')






