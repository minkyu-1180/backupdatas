# sw academy 4839. 이진탐색

import sys
sys.stdin = open("binarysearchinput.txt")


def BinarySearch(P, p):
    l = 1
    r = P
    c = 1
    while l <= r:
        middle = (l + r) // 2
        if middle == p:
            return c
        elif middle > p:
            r = middle
        elif middle < p:
            l = middle
        c += 1


T = int(input())
for test_case in range(1, T+1):
    # P : 페이지의 총 쪽수 / Pa : A가 찾아야 하는 쪽수 / Pb : B가 찾아야 하는 쪽수
    P, Pa, Pb = map(int, input().split())

    # P : 페이지의 총 쪽 수, p : 찾아야 하는 쪽수

    count_a = BinarySearch(P, Pa)
    count_b = BinarySearch(P, Pb)
    if count_a == count_b:
        print(f'#{test_case} 0')
    elif count_a < count_b:
        print(f'#{test_case} A')
    elif count_a > count_b:
        print(f'#{test_case} B')

