# GNS
import sys
sys.stdin = open("GNSinput.txt")
T = int(input())
for test_case in range(1, T+1):
    tc_N = input()
    str_list = input().split()

    other_planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_arr = [0] * 10
    result = [0] * len(str_list)
    # 각 숫자를 지정하는 단어의 개수 세기
    for i in range(10):
        for j in range(len(str_list)):
            if str_list[j] == other_planet[i]:
                count_arr[i] += 1

    print(f'#{test_case}')
    for i in range(10):
        for _ in range(count_arr[i]):
            print(other_planet[i], end = ' ')
    print()







