# 파스칼의 삼각형
import sys
sys.stdin = open("pascaltriangleinput.txt")

# 파스칼의 삼각형을 각 층의 값들을 순서대로 배열에 담은 배열(원소 : 모두 배열)
def pascal_t(n):
    if n == 1:
        result =  [[1]]
    else:
        result = pascal_t(n-1)
        nth_row = [1] + [0] * (n-2) + [1]
        for i in range(1, n-1):
            nth_row[i] = result[n-2][i-1] + result[n-2][i]
        result.append(nth_row)
    return result

T = int(input())
for test_case in range(1, T+1):
    # 파스칼 삼각형의 줄 수
    N = int(input())
    result = pascal_t(N)

    print(f'#{test_case}')
    for i in result:
        print(*i)
