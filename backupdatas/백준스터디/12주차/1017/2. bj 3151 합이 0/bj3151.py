# 백준 3151. 합이 0
import sys
sys.stdin = open("bj3151input.txt")



N = int(input())
arr = list(map(int, input().split()))
if N < 3:
    result = 0
else:
    arr.sort()
    result = 0
    for i in range(0, N-2):
        s = i+1
        e = N-1
        num1 = arr[i]
        if arr[i] > 0:
            break

        while s < e:
            num2 = arr[s] + arr[e]
            # 합이 0
            if num1 + num2 == 0:
                # 아예 쭉 같으면(s ~ e의 모든 값 동일)
                if arr[s] == arr[e]:
                    result += (e-s+1)*(e-s)//2
                    break
                else:

                    # 지금 기준으로 얼마나 더 이동하면서 볼 것인가?
                    # s_move : s ->
                    # e_move : <- e
                    s_move = 0
                    e_move = 0

                    # s 기준 오른쪽의 같은 값들은 쭉 이동하여 한 번에 결과에 반환
                    while arr[s] == arr[s+1]:
                        s += 1
                        s_move += 1
                    # e 기준 왼쪽의 같은 값들은 쭉 이동하여 한 번에 결과 반환
                    while arr[e] == arr[e-1]:
                        e -= 1
                        e_move += 1
                    '''
                    현재 상태
                    arr[s] ~ arr[s+s_move]까지 같고,
                    arr[e-e_move] ~ arr[e]까지 같음(근데 서로 다름 -> 순열 느낌으로 곱)
                    -> 결과에 추가되는 경우의 수 :  (s_move+1) * (e_move+1)
                    '''
                    result += (s_move+1) * (e_move+1)
                    # 추가로 이동
                    s += 1
                    e -= 1
            # num1 기준으로 num2를 더하면 양수 -> 끝값 줄이기
            elif num1 + num2 > 0:
                e -= 1
            # num1 기준으로 num2를 더하면 음수 -> 처음값 키우기
            elif num1 + num2 < 0:
                s += 1
print(result)