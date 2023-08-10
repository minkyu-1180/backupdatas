# 1157. 단어공부
import sys
sys.stdin = open("1157input.txt")

T = int(input())
for test_case in range(1, T+1):
    string = input().upper()
    string_only = list(set(string))
    num_of_string = []
    max_val = 0
    result = ''
    for s in string_only:
        num_of_string.append(string.count(s))

    max_c = max(num_of_string)


    if num_of_string.count(max_c) != 1:
        print('?')
    else:
        print(string_only[num_of_string.index(max_c)])

