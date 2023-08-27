# IM 대비 28. 영준이의 카드카운팅
import sys
sys.stdin = open("영준이input.txt")

T = int(input())
for test_case in range(1, T+1):
    string = input()
    arr = []
    for i in range(0, len(string), 3):
        arr.append(string[i:i+3])

    if len(arr) != len(set(arr)):
        print(f'#{test_case} ERROR')
    else:
        # 각 카드 종류 초기값
        types = {'S' : 13,
                'D' : 13,
                'H' : 13,
                'C' : 13
                }
        for card in arr:
            type = card[0]
            types[type] -= 1

        print(f"#{test_case} {types['S']} {types['D']} {types['H']} {types['C']} ")
