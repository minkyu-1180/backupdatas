# sw academy - 0802. 부분집합의 합
# 다시 풀기 아직 안품

import sys
sys.stdin = open("subsetinput.txt")

def issumzero(my_list):
    result = []
    return_val = 0
    N = len(my_list)
    c = 0
    while c < N:

        for i in my_list:
            result.append(i)
        for i in my_list:
            for j in my_list:
                if i != j:
                    result.append(i + j)
        for i in my_list:
            for j in my_list:
                if i != j:
                    for k in my_list:
                       if k != i and k != j:
                           result.append(i + j + k)

        # 해당 요소들로 만들 수 있는 덧셈 연산의 모든 결과 내에 0이 있을 경우
        if 0 in result:
            return_val = 1
            break
        else:
            c += 1
    return return_val





    pass


T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    print(f'#{test_case} {issumzero(arr)}')