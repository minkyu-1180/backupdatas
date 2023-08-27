# IM 대비 30. 패턴마디의 길이
import sys
sys.stdin = open("패턴마디의길이input.txt")

T = int(input())
for test_case in range(1,T+1):
    string = input()

    # 패턴마디 길이가 1일 경우
    if string[0] * len(string) == string:
        result = 1
    else:
        for i in range(2, 11):
            if string[0:i] == string[i:2*i]:
                result = i
                break
    print(f'#{test_case} {result}')
