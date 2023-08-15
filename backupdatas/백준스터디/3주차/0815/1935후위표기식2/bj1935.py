# 백준 1935. 후위 표기법 2
import sys
sys.stdin = open('1935input.txt')

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    string = input()
    # ord('A') : 65 ~ ord('Z') : 90
    # string 내부의 피연산자는 무조건 A부터, N의 개수만큼의 수가 들어가있음
    alphabet = [int(input()) for _ in range(N)]
    stack = []

    for s in string:
        # s가 피연산자일 경우
        if s.isalpha():
            # 해당 피연산자가 대응되는 알파벳에 접근
            # ord('A')기준으로 하여 뺀 후 인덱스에 접근
            stack.append(alphabet[ord(s) - 65])

        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if s == '+':
                stack.append(num1 + num2)
            elif s == '-':
                stack.append(num1 - num2)
            elif s == '*':
                stack.append(num1 * num2)
            elif s == '/':
                stack.append(num1 / num2)
    print('%.02f' %stack[0])
