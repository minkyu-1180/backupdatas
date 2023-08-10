import sys
sys.stdin = open("stringtestinput.txt")

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    result = 0
    i = 0
    while i <= len(str2) - len(str1):
        new_str = ''
        for j in range(i, i + len(str1)):
            new_str += str2[j]
        if new_str == str1:
            result = 1
            break
        else:
            i += 1
    print(f'#{test_case} {result}')