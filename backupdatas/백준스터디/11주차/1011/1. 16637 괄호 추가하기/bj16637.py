# 백준 16637. 괄호 추가하기
import sys
sys.stdin = open("bj16697input.txt")
sys.setrecursionlimit(10**6)
def backtracking(idx, sum_of_num, last_operator):
    global result, is_bracket

    if idx == N-2:
        if result < sum_of_num:
            result = sum_of_num
        return

    i = idx + 2
    operator = arr[i]
    # (n1 + n2) + n3
    if last_operator == '+' and operator == '+':
        is_bracket = False
        backtracking(i, sum_of_num + arr[i+1], operator)
    # (n1 + n2) - n3
    elif last_operator == '+' and operator == '-':
        is_bracket = False
        backtracking(i, sum_of_num - arr[i+1], operator)
    # (n1 + n2) * n3 -> n1 + (n2 * n3) or 그대로
    elif last_operator == '+' and operator == '*':
        if is_bracket:
            is_bracket = False
            backtracking(i, sum_of_num * arr[i+1], operator)
        else:
            backtracking(i, sum_of_num * arr[i+1], operator)
            num1 = sum_of_num - arr[i-1]
            num2 = arr[i-1]
            num3 = arr[i+1]
            is_bracket = True
            backtracking(i, num1 + num2 * num3, operator)
    # 직전 연산자가 -
    elif last_operator == '-' and operator == '-':
        if is_bracket:
            is_bracket = False
            backtracking(i, sum_of_num - arr[i+1], operator)
        else:
            backtracking(i, sum_of_num - arr[i+1], operator)
            is_bracket = True
            num1 = sum_of_num + arr[i-1]
            num2 = arr[i-1]
            num3 = arr[i+1]
            backtracking(i, num1-(num2-num3), operator)
    elif last_operator == '-' and operator == '+':
        if is_bracket:
            is_bracket = False
            backtracking(i, sum_of_num + arr[i+1], operator)
        else:
            backtracking(i, sum_of_num + arr[i+1], operator)
            is_bracket = True
            num1 = sum_of_num + arr[i-1]
            num2 = arr[i-1]
            num3 = arr[i+1]
            backtracking(i, num1-(num2+num3), operator)
    elif last_operator == '-' and operator == '*':
        if is_bracket:
            is_bracket = False
            backtracking(i, sum_of_num * arr[i+1], operator)
        else:
            backtracking(i, sum_of_num * arr[i+1], operator)
            is_bracket = True
            num1 = sum_of_num + arr[i-1]
            num2 = arr[i-1]
            num3 = arr[i+1]
            backtracking(i, num1 - num2 * num3, operator)

    # 직전 연산자가 *
    elif last_operator == '*' and operator == '*':
        is_bracket = False
        backtracking(i, sum_of_num * arr[i+1], operator)
    elif last_operator == '*' and operator == '+':
        if is_bracket:
            is_bracket = False
            backtracking(i, sum_of_num + arr[i+1], operator)
        else:
            backtracking(i, sum_of_num + arr[i+1], operator)
            if arr[i-1]:
                is_bracket = True
                num1 = sum_of_num // arr[i-1]
                num2 = arr[i-1]
                num3 = arr[i+1]
                backtracking(i, num1 * (num2 + num3), operator)

    elif last_operator == '*' and operator == '-':
        if is_bracket:
            is_bracket = False
            backtracking(i, sum_of_num - arr[i+1], operator)
        else:
            backtracking(i, sum_of_num - arr[i+1], operator)
            is_bracket = True
            num1 = sum_of_num // arr[i-1]
            num2 = arr[i-1]
            num3 = arr[i+1]
            backtracking(i, num1 * (num2 - num3), operator)


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(input())
    for i in range(0, N, 2):
        arr[i] = int(arr[i])

    # 안썼으면, 괄호 쓰거나 안쓰거나 둘 중 하나
    is_bracket = False
    result = 0
    if arr[1] == '+':
        last_operator = '+'
        sum_of_num = arr[0] + arr[2]
    elif arr[1] == '-':
        last_operator = '-'
        sum_of_num = arr[0] - arr[2]
    else:
        last_operator = '*'
        sum_of_num = arr[0] * arr[2]
    backtracking(1, sum_of_num, last_operator)
    print(result)

# 현재 몇 번째 idx에 있는 연산자까지 결정했어?
def backtracking(idx, c, is_bracket):
    if idx == N-2:
        return

    if c == N//2:
        return

    if is_bracket:
        backtracking(idx+1, c, not is_bracket)
    else:
