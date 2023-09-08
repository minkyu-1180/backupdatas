# 백준 2512. 예산
import sys
sys.stdin = open("bj2512input.txt")

T = int(input())
for tc in range(T):
    N = int(input()) # 지방 수
    arr = list(map(int, input().split()))
    M = int(input())
    result = 0

    # 모든 요청 예산 배정 가능
    if M >= sum(arr):
        result = arr[-1]
        print(result)
    # 배정금 설정
    else:
        arr.sort()
        small = arr[0]
        # 가장 작은 예산요청금액으로 배정해도 문제가 생기는 경우
        if N * small > M:
            # 모든 지방이 배정금으로 예산을 받게 됨
            result = M//N
            print(result)
        else:
            s = e = 0
            idx = 0
            for i in range(1, N):
                # i번째로 요청 금액이 큰 지방 기준으로 배정금을 잡을 경우의 총 배정금 합
                sum_bajung = sum(arr[0:i]) + (N-i) * arr[i]
                if sum_bajung > M:
                    s = arr[i-1]
                    e = arr[i]
                    idx = i
                    break
            # 이진탐색 진행
            while s <= e:
                # 배당 금액 잡기(arr[idx-1] <= middle < arr[idx+1])
                middle = (s + e)//2
                # idx 기준 왼쪽 : 그냥 그대로 받음
                # idx 기준(포함) 오른쪽 : 배당금대로 받음
                bajung_sum = sum(arr[0:idx]) + (N-idx) * middle

                # 해당 값을 기준으로 배당금을 나눠주었을 때 완벽하게 예산과 맞는 경우 -> 최적
                if bajung_sum == M:
                    result = middle
                    break

                if bajung_sum > M:
                    e = middle-1

                elif bajung_sum < M:
                    if result < middle:
                        result = middle
                    s = middle+1


            print(result)


