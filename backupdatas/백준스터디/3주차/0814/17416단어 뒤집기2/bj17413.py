# 백준 17416. 단어 뒤집기 2
# import sys
# sys.stdin = open("17413input.txt")
#
# T = int(input())
# for test_case in range(1, T+1):
    # len(S) <= 100000
S = input()

result = ''
istag = False

i = 0
while i < len(S):
    # 태그 시작
    if S[i] == '<':
        stack = ''
        end = i + 1
        for idx in range(i, len(S)):
            stack += S[idx]
            if S[idx] == '>':
                end = idx
                break
        i = end
        result += stack
    # 태그 밖 빈칸
    elif S[i] != ' ':
        stack = ''
        end = i + 1
        for idx in range(i, len(S)):
            if S[idx] != ' ' and S[idx] != '<':
                stack = S[idx] + stack
            elif S[idx] == ' ':
                stack += S[idx]
                end = idx
                break
            elif S[idx] == '<':
                end = idx-1
                break
        else:
            result += stack
            break

        i = end
        result += stack
    i += 1

print(result)























'''
    while i < len(S):
        # 1. i번 인덱스의 값이 <, >, 빈칸이 아닌 경우
        if S[i] != '<' and S[i] != '>' and S[i] != ' ':
            new_string = ''
            # 역순으로 추가할 문자들의 시작, 마지막 인덱스 초기화
            start = i
            end = i + 1
            for idx in range(i+1, len(S)):
                # 아직은 그냥 문자인 경우
                if S[idx] == '<' or S[idx] == ' ':
                    end = idx - 1
                    break
            # 현재 start, end : 빈칸, <, >가 아닌 문자들로만 이루어진 문자열의 시작, 끝 idx
            for idx in range(end, start - 1, -1):
                new_string += S[idx]
            result.append(new_string)
            i = end
        elif S[i] == ' ':
            result.append(S[i])

        elif S[i] == '<':
            new_string = ''
            for idx in range(i, len(S)):
                new_string += S[idx]
                if S[idx] == '>':
                    i = idx
                    break
            result.append(new_string)

        i += 1
    print(result)

'''
'''     

    while i < len(S):
        # 1. i번 인덱스의 값이 <,>가 아닐 경우
        if S[i] != '<' and S[i] != '>':
            # 빈 칸인 경우는 그냥 추가
            if S[i] == ' ':
                result += ' '
            # 빈칸이 아닌 경우 : 빈칸을 만나거나 <를 만날 때 까지 진행
            else:
                new_string = ''
                start = i
                end = i + 1
                for idx in range(i + 1, len(S)):
                    if S[idx] == '<' or S[idx] == ' ': # 처음으로 <를 만나게 될 경우
                        end = idx - 1
                        break
                    # 끝까지 다 이어져 있을 경우
                for idx in range(end, start-1, -1):
                    new_string += S[idx]
                result += new_string
                i = end
        elif S[i] == '<':
            new_string = ''
            for idx in range(i, len(S)):
                new_string += S[idx]
                if S[idx] == '>':
                    i = idx
                    break
            result += new_string
        i += 1


    print(result)


'''


'''


    i = 0
    while i < len(S):

        if S[i] == '<':
            new_string = ''
            while S[i] != '>':
                new_string += S[i]
                i += 1
                if S[i] == '>':
                    new_string += '>'
                    result.append(new_string)
            i += 1
        elif S[i] != '>':
            new_string = ''
'''



