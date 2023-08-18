# 백준 1966. 프린터큐
import sys
sys.stdin = open("1966input.txt")

T = int(input())
for tc in range(T):
    # N : 문서의 개수(1 ~ 100)
    # M : 인쇄된 순서(0번부터 시작)
    N, M = map(int, input().split())
    # arr의 idx :
    # arr의 원소 : 중요도(1 ~ 9) / 중복된 중요도가 있을 수도 있음 / 높을수록 중요
    arr = list(map(int, input().split()))
    # print(arr)
    new_arr = [[arr[i], i] for i in range(len(arr))]
    #print(new_arr)
    queue = [0] * (N+1)

    front = 0
    num = 9
    que_idx = 1
    while num > 0:
        input_front = front
        for i in range(front, len(new_arr)):
            if num == new_arr[i][0]:
                input_front = i
                queue[que_idx] = new_arr[i][1]
                if new_arr[i][1] == M:
                    print(que_idx)
                    break
                que_idx += 1

        for i in range(front):
            if num == new_arr[i][0]:
                input_front = i
                queue[que_idx] = new_arr[i][1]
                if new_arr[i][1] == M:
                    print(que_idx)
                    break
                que_idx += 1

        front = input_front
        num -= 1




