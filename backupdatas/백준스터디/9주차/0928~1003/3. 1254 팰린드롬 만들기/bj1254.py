# 백준 1254. 팰린드롬 만들기
import sys
sys.stdin = open("bj1254input.txt")

T = int(input())
for tc in range(T):
    string = input()
    N = len(string)

    if string == string[::-1]:
        result = len(string)
    else:
        for i in range(N):
            string_2 = string + string[i::-1]
            if string_2 == string_2[::-1]:
                result = len(string_2)
                break
    print(result)

