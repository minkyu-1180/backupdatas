# 1316. 그룹 단어 체커
import sys
sys.stdin = open("1316input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 그룹 단어의 개수
    result = 0

    for _ in range(N):
        isgroup = 1
        string = input()
        string_set = list(set(string))
        s_dict = dict()
        for s in string:
            s_dict[s] = string.count(s)

        for s in string:
            if s * s_dict[s] not in string:
                isgroup = 0
        if isgroup == 1:
            result += 1
    print(result)



