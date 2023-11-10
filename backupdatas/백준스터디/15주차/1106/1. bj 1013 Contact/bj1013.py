# 백준 1013. Contact
import sys
sys.stdin = open("bj1013input.txt")

def backtracking(mystr, idx):
    global result
    if idx >= N:
        if mystr == string:
            result = 'YES'
        return

    # 남은 index가 1개, 2개, 3개일 경우 -> 짝 맞추기 실패(무조건 남은 부분이 01이나 1001, 10001, 10011, ...이 되어야 해서)
    if N-1 - idx == 0 or N-1 - idx == 2:
        return

    # idx : 현재 string[idx]를 보는 중이다.
    # 1. string[idx:idx+2] == '01' -> 통과
    if string[idx:idx+2] == '01':
        backtracking(mystr+'01', idx+2)

    # 2. string[idx:idx+3] == '100' --> 그 뒤 이어지는 0을 쭉 더해주고, 1이 나오는 지점부터 다음 0이 나올 때 까지 backtracking
    elif string[idx:idx+3] == '100':
        idx += 3
        mystr += '100'
        flag = False # 앞에서 1을 최소 한 번 만났는가? 10 + 0*x + 1이 되었는가?에 대한 기준
        for i in range(idx, N):
            # 0이 나왔는데, 앞에서 이미 1이 나옴(00000,.....,111110인 순간)
            if string[i] == '0' and flag:
                return
            elif string[i] == '0' and not flag:
                mystr += '0'
                idx+=1
            elif string[i] == '1':
                flag = True
                idx += 1
                backtracking(mystr+'1', idx)
        else:
            return
    else:
        return






# 테스트 케이스 개수
T = int(input())
for tc in range(T):
    # string : 전파를 표현하는 0과 1 만으로 이루어진 문자열(1 <= len(string) <= 200)
    string = input()
    N = len(string)

    if N == 1 or N == 3:
        print('NO')
    elif N == 2 and string != '01':
        print('NO')

    else:


        pattern = '(100+1+|01)+'

        A_1 = '100'
        B_1 = '01'

        result = 'NO'
        idx = 0
        backtracking('', idx)
        print(result)

