# 백준 2596. 비밀편지
import sys
sys.stdin = open("bj2596input.txt")

secret_key = {
    '000000' : 'A',
    '001111' : 'B',
    '010011' : 'C',
    '011100' : 'D',
    '100110' : 'E',
    '101001' : 'F',
    '110101' : 'G',
    '111010' : 'H',
}

T = int(input())
for tc in range(T):
    N = int(input())
    string = input()
    result1 = ''
    result2 = 0
    for i in range(0, 6*N, 6):
        chr = string[i:i+6]
        if chr in secret_key:
            result1 += secret_key[chr]
        else:

            for key in secret_key:
                c = 0
                for k in range(6):
                    if key[k] != chr[k]:
                        c += 1
                        if c >= 2:
                            break
                else:
                    result1 += secret_key[key]
                    break
            else:
                result2 = i//6 + 1
                break
    if result2:
        print(result2)
    else:
        print(result1)


