# sw academy 단순 2진 암호코드
import sys
sys.stdin = open("단순2진암호코드input.txt")
T = int(input())

code_key = {'0001101' : 0,
            '0011001' : 1,
            '0010011' : 2,
            '0111101' : 3,
            '0100011' : 4,
            '0110001' : 5,
            '0101111' : 6,
            '0111011' : 7,
            '0110111' : 8,
            '0001011' : 9}

for test_case in range(1, T+1):
    # N : 행 크기 (1≤N≤50), M : 열 크기 (56≤M≤100)
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = []

    row = 0
    for i in range(N):
        if '1' in arr[i]:
            row = i
            break
    end_c = M-1
    for j in range(M-1, -1, -1):
        if arr[row][j] == '1':
            end_c = j
            break
    start_c = end_c - 55

    string = arr[row]
    secretcode = string[start_c:end_c+1]
    for i in range(0, 50, 7):
        start = i
        end = i + 6
        code = secretcode[start:end+1]
        for key in code_key.keys():
            if key == code:
                result.append(code_key[key])

    sum_codes = 0
    sum_val = 0
    for i in range(4):
        sum_codes += (3 * result[2 * i] + result[2 * i + 1])
        sum_val += (result[2 * i] + result[2 * i + 1])
    if sum_codes % 10 != 0:
        sum_val = 0

    print(f'#{test_case} {sum_val}')







