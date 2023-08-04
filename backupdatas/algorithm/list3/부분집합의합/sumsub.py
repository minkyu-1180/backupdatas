# sw academy - 0802. 부분집합의 합
import sys
sys.stdin = open("sumsubinput.txt")
T = int(input())
def zerosum_sub(my_arr):
    n = len(my_arr)
    all_subs = []
    # 공집합을 제외한 모든 부분집합의 개수 : n**2 - 1
    for i in range(1, 1 << n):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(my_arr[j])
        all_subs.append(sub)
    return all_subs


for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    mysubs = zerosum_sub(arr)
    result = 0
    for sub in mysubs:
        sub_ele_sum = 0
        for i in range(len(sub)):
            sub_ele_sum += sub[i]
        if sub_ele_sum == 0:
            result = 1
        else:
            continue
    print(f'#{test_case} {result}')